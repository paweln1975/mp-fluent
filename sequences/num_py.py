import numpy as np
class NumPyExt:
    @staticmethod
    def convert_consecutive_to_two_dimensional_array(count: int) -> np.ndarray:
        """
        Convert a list of consecutive numbers into a 2D NumPy array.

        >>> count = 12
        >>> np_arr = NumPyExt.convert_consecutive_to_two_dimensional_array(count)
        >>> np_arr
        array([[ 1,  2,  3],
               [ 4,  5,  6],
               [ 7,  8,  9],
               [10, 11, 12]])
        """
        a = np.arange(1, count + 1)
        a.shape = 4, 3  # Reshape to 4 rows and 3 columns
        # Note: If count is not a multiple of 12, this will raise an error
        return a

    @staticmethod
    def convert_consecutive_to_two_dimensional_array_with_reshape_and_transpose(count: int) -> np.array:
        """
        Convert a list of consecutive numbers into a 2D NumPy array using reshape and transpose.

        >>> count = 12
        >>> np_arr = NumPyExt.convert_consecutive_to_two_dimensional_array_with_reshape_and_transpose(count)
        >>> np_arr
        array([[ 1,  4,  7, 10],
               [ 2,  5,  8, 11],
               [ 3,  6,  9, 12]])
        """
        a = np.arange(1, count + 1)
        a.shape = 4, 3
        return a.transpose()

    @staticmethod
    def save_10M_floats_to_file(filename: str) -> None:
        """
        Save 10 million random floats to a binary file.

        >>> NumPyExt.save_10M_floats_to_file('test_floats.npy')
        np.True_
        """
        floats = np.random.rand(10_000_000).astype(np.float32)
        floats *= 6
        np.save(filename, floats)

        # Verify by loading the file back
        loaded_floats = np.load(filename)

        return np.less_equal(loaded_floats, 6.0).all()


