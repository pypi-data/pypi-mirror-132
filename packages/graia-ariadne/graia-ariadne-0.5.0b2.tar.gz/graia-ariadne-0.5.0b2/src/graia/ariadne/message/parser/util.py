"""消息链处理器用到的工具函数, 类"""
import argparse
import inspect
import re
from contextvars import ContextVar
from typing import List, NoReturn, Type, Union

from ..chain import Element_T, MessageChain

elem_mapping_ctx: ContextVar["MessageChain"] = ContextVar("elem_mapping_ctx")


def split(string: str) -> List[str]:
    """尊重引号与转义的字符串切分

    Args:
        string (str): 要切割的字符串

    Returns:
        List[str]: 切割后的字符串, 可能含有空格
    """
    result: List[str] = []
    quote = ""
    cache: List[str] = []
    for index, char in enumerate(string):
        if char in "'\"":
            if not quote:
                quote = char
            elif char == quote and index and string[index - 1] != "\\":  # is current quote, not transfigured
                quote = ""
            else:
                cache.append(char)
            continue
        if not quote and char == " ":
            result.append("".join(cache))
            cache = []
        else:
            if char != "\\":
                cache.append(char)
    if cache:
        result.append("".join(cache))
    return result


def gen_flags_repr(flags: re.RegexFlag) -> str:
    """通过 RegexFlag 生成对应的字符串

    Args:
        flags (re.RegexFlag): 正则表达式的标记

    Returns:
        str: 对应的标记字符串
    """
    flags_list: List[str] = []

    if re.ASCII in flags:
        flags_list.append("a")
    if re.IGNORECASE in flags:
        flags_list.append("i")
    if re.LOCALE in flags:
        flags_list.append("L")
    if re.MULTILINE in flags:
        flags_list.append("m")
    if re.DOTALL in flags:
        flags_list.append("s")
    if re.UNICODE in flags:
        flags_list.append("u")
    if re.VERBOSE in flags:
        flags_list.append("x")

    return "".join(flags_list)


def transformed_regex(flag: re.RegexFlag, regex_pattern: str) -> str:
    """生成嵌套正则表达式字符串来达到至少最外层含有一个捕获组的效果

    Args:
        flag (re.RegexFlag): 正则表达式标记
        regex_pattern (str): 正则表达式字符串

    Returns:
        str: 转换后的正则表达式字符串
    """
    if flag:
        regex_pattern = f"(?{gen_flags_repr(flag)}:({regex_pattern}))"
    else:
        regex_pattern = f"({regex_pattern})"
    return regex_pattern


class MessageChainType:
    """用于标记类型为消息链, 在 ArgumentMatch 上使用"""

    def __init__(self, regex: re.Pattern):
        self.regex: re.Pattern = regex

    def __call__(self, string: str) -> MessageChain:
        if self.regex and not self.regex.fullmatch(string):
            raise ValueError(f"{string} not matching {self.regex.pattern}")
        return MessageChain.fromMappingString(string, elem_mapping_ctx.get())


class ElementType:
    """用于标记类型为消息链元素, 在 ArgumentMatch 上使用"""

    def __init__(self, pattern: Type[Element_T]):
        self.regex = re.compile(f"\x02(\\d+)_{pattern.__fields__['type'].default}\x03")

    def __call__(self, string: str) -> MessageChain:
        if not self.regex.fullmatch(string):
            raise ValueError(f"{string} not matching {self.regex.pattern}")
        return MessageChain.fromMappingString(string, elem_mapping_ctx.get())[0]


class TwilightParser(argparse.ArgumentParser):
    """适于 Twilight 使用的 argparse.ArgumentParser 子类
    移除了报错时自动退出解释器的行为
    """

    def error(self, message) -> NoReturn:
        raise ValueError(message)

    def accept_type(self, action: Union[str, type]) -> bool:
        """检查一个 action 是否接受 type 参数

        Args:
            action (Union[str, type]): 检查的 action

        Returns:
            bool: 是否接受 type 参数
        """
        if isinstance(action, str):
            action_cls: Type[argparse.Action] = self._registry_get("action", action, action)
        elif issubclass(action, argparse.Action):
            action_cls = action
        else:
            return False
        action_init_sig = inspect.signature(action_cls.__init__)
        if "type" not in action_init_sig.parameters:
            return False
        return True
