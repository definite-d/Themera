"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Filters File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
from typing import Callable, Dict, List, Optional, Tuple, Union

import colour

from .functions import (
    check_if_color,
    flatten_themedict,
    invert,
    rint,
    unflatten_themedict,
)
from .settings import SETTINGS


# FILTERS ______________________________________________________________________________________________________________
def index_filter(themedict: Dict, index: List) -> Dict:
    """
    This function essentially rearranges the colors in a given themedict according to positions (each position is a
    floating point number ranging from 0 <starting position; index 0> to 1 <ending position; last index>) listed in an
    index list.

    To give a simple example, given an `index` list `[0.2, 0.8, 0.6, 0.4, 0.5]` and a list of colors
    (extracted from the `themedict`) as `['black', 'red', 'yellow', 'cyan', 'white']`, an index filter will rearrange
    those colors to give: `['black', 'cyan', 'yellow', 'red', 'yellow']`

    :param themedict: A themedict to work on.
    :param index: A list of floating point numbers ranging from 0 to 1.
    :return: A re-arranged dict.
    """

    flat = flatten_themedict(themedict)
    colors = {k: v for k, v in flat.items() if check_if_color(v)}
    sorted_colors = sorted(
        list(set(colors)), key=lambda x: colour.Color(colors[x]).get_luminance()
    )
    mapped = []
    if len(sorted_colors) <= len(index):
        # If we have a list of colors less than the list of indexes:
        for _index in index[0 : len(sorted_colors)]:
            mapped.append(colors[sorted_colors[rint(_index * len(sorted_colors)) - 1]])
    else:
        # Otherwise, we need to 'scale' the index list to the colors list.
        for n in range(len(colors)):
            # Suppose we mentally traverse both the color and index lists simultaneously:
            # This is a fraction representing how far we've traversed the color list at the present n:
            current_point = n + 1 / len(sorted_colors)
            # We can apply the same fraction to the index list and get the corresponding position in the index list.
            index_position = rint(current_point * len(index))
            # The index list is a list of floating point numbers that indicate which point of the sorted colors should be
            # applied at the current index, like a guide on how to "rearrange" the colors by their indexes.
            # We'll call that point "mapped_point".
            mapped_point = index[
                index_position - 1
            ]  # Minus 1 because indexes start at 0.
            # Now we convert the point to a position in the color list.
            mapped_position = rint(mapped_point * len(sorted_colors))
            # And use that position to get the item that should be at that position.
            item = sorted_colors[
                mapped_position - 1
            ]  # Minus 1 because indexes start at 0.
            # Get the color for that item.
            color = colors[item]
            # Finally, add the color to the mapped (result) list.
            mapped.append(color)

    register = dict(zip(colors.keys(), mapped))
    result = flat.copy()
    result.update(register)
    return unflatten_themedict(result, themedict)


def autocontrast_filter(themedict: Dict):
    """
    Applies a luminance adjustment filter to tweak the "contrast" of the colors.

    :param themedict: The themedict to apply the filter to.
    :return:
    """
    flat = flatten_themedict(themedict)
    luminance = colour.Color(list(flat.values())[0]).get_luminance()
    if luminance < 0.5:
        lum = [max(round(luminance, 2) * 0.8, 0)] + SETTINGS["autocontrast_index_dark"]
    else:
        lum = [min(round(luminance, 2) * 1.443, 1)] + SETTINGS[
            "autocontrast_index_light"
        ]
    colors = {k: v for k, v in flat.items() if check_if_color(v)}
    # sorted_colors = sorted(list(set(colors)), key=lambda x: colour.Color(colors[x]).get_luminance())
    contrasted = list()
    for index, color in enumerate(colors.values()):
        if len(lum) < len(colors):
            colour_object = colour.Color(color)
            mapped_index = rint(((index + 1) / len(colors)) * len(lum)) - 1
            colour_object.set_luminance(lum[mapped_index])
            contrasted.append(colour_object.get_web())
        else:
            colour_object = colour.Color(color)
            colour_object.set_luminance(lum[index])
            contrasted.append(colour_object.get_web())
    register = dict(zip(colors.keys(), contrasted))
    result = flat.copy()
    result.update(register)
    return unflatten_themedict(result, themedict)


def dark_mode_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    return index_filter(themedict, index=SETTINGS["dark_mode_index"])


def light_mode_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    return index_filter(themedict, index=SETTINGS["light_mode_index"])


def individual_filter(
    action: Callable,
    themedict: Dict[str, Union[str, Tuple, List]],
    additional_args: Optional[Dict[str, Union[str, Tuple, List]]] = None,
):
    flat = flatten_themedict(themedict)
    if additional_args:
        colors = {
            k: action(v, **additional_args)
            for k, v in flat.items()
            if check_if_color(v)
        }
    else:
        colors = {k: action(v) for k, v in flat.items() if check_if_color(v)}
    result = flat.copy()
    result.update(colors)
    result = unflatten_themedict(result, themedict)
    return result


def inverted_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    return individual_filter(invert, themedict)


def gray_out_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    def _action(color):
        color = colour.Color(color)
        color.set_saturation(0)
        return color.get_web()

    return individual_filter(_action, themedict)


def transform_filter(color: str, transformation_matrix: List[List[float]]):
    color = colour.web2rgb(color)
    result = []
    for row in transformation_matrix:
        sub_result = 0
        for index, element in enumerate(row):
            sub_result += element * color[index]
        result.append(sub_result)
    return colour.rgb2web(tuple(result))


def protanopia_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.56667, 0.43333, 0], [0.55833, 0.44167, 0], [0, 0.24167, 0.75833]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def protanomaly_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.81667, 0.18333, 0], [0.33333, 0.66667, 0], [0, 0.125, 0.875]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def deuteranopia_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def deuteranomaly_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.8, 0.2, 0], [0, 0.25833, 0.74167], [0, 0.14167, 0.85833]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def tritanopia_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.95, 0.05, 0], [0, 0.43333, 0.56667], [0, 0.475, 0.525]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def tritanomaly_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.96667, 0.03333, 0], [0, 0.73333, 0.26667], [0, 0.18333, 0.81667]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def achromatopsia_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.299, 0.587, 0.114], [0.299, 0.587, 0.114], [0.299, 0.587, 0.114]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


def achromatomaly_filter(themedict: Dict[str, Union[str, Tuple, List]]):
    matrix = [[0.618, 0.32, 0.062], [0.163, 0.775, 0.062], [0.163, 0.32, 0.516]]
    return individual_filter(
        transform_filter, themedict, {"transformation_matrix": matrix}
    )


FILTER_MAPPING = {
    "-- No Filters --": None,
    "Auto Contrast": autocontrast_filter,
    "Dark Mode": dark_mode_filter,
    "Light Mode": light_mode_filter,
    "Gray Out": gray_out_filter,
    "Inverted": inverted_filter,
    "Achromatomaly": achromatomaly_filter,
    "Achromatopsia": achromatopsia_filter,
    "Deuteranomaly": deuteranomaly_filter,
    "Deuteranopia": deuteranopia_filter,
    "Protanomaly": protanomaly_filter,
    "Protanopia": protanopia_filter,
    "Tritanomaly": tritanomaly_filter,
    "Tritanopia": tritanopia_filter,
}

FILTERS = list(FILTER_MAPPING.keys())
