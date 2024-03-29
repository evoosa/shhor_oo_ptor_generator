from shhor_ptor.config import fill_chr
from shhor_ptor.utils.get_pixels import *


def fill_row(row, max_row_len, img_width):
    """ fill an array of rows with empty cells, to build the shhor-ptor diagram """
    row_beginning = (max_row_len - len(row)) * [fill_chr]
    row_ending = img_width * [fill_chr]
    return row_beginning + row + row_ending


def fill_rows(b_rows, img_width):
    """ fill all arrays of the rows of black cells, in order to build the diagram """
    max_row_len = len(max(b_rows, key=len))
    for i in range(len(b_rows)):
        row = b_rows[i]
        b_rows[i] = fill_row(row, max_row_len, img_width)
    return b_rows


def columns_to_rows(b_columns, max_row_len):
    """ convert array of columns, to rows - READY TO BE PUSHED TO THE DIAGRAM"""
    longest_col_len = len(max(b_columns, key=len))
    for i in range(len(b_columns)):
        col = b_columns[i]
        filling = (longest_col_len - len(col)) * [fill_chr]
        b_columns[i] = filling + col
    return [(max_row_len * [fill_chr] + [col[j] for col in b_columns]) for j in range(longest_col_len)]


def get_diagram(img_obj):
    """ build a shhor-ptor diagram using the img_obj """

    # get the number of blacks in the rows and columns of the image
    b_rows = get_black_rows(get_pixel_rows(img_obj))
    b_columns = get_black_columns(get_pixel_columns(img_obj))

    max_row_len = len(max(b_rows, key=len))
    filled_coloumn_rows = columns_to_rows(b_columns, max_row_len) # columns who are converted to rows, in order to build the diagram
    filled_rows = fill_rows(b_rows, img_obj.size[0])

    return filled_coloumn_rows + filled_rows
