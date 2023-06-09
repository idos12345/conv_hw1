import random

import numpy as np
import torch
from torch.utils.data import Dataset
import itertools
import helpers.plot as plot
import hw1.datasets as hw1datasets


class RandomImageDataset(Dataset):
    """
    A dataset returning random noise images of specified dimensions
    """

    def __init__(self, num_samples, num_classes, C, W, H):
        """
        :param num_samples: Number of samples (labeled images in the dataset)
        :param num_classes: Number of classes (labels)
        :param C: Number of channels per image
        :param W: Image width
        :param H: Image height
        """
        super().__init__()
        self.num_classes = num_classes
        self.num_samples = num_samples
        self.image_dim = (C, W, H)

    def __getitem__(self, index):
        # TODO: Create a random image tensor and return it.
        # Bonus if you make sure to always return the same image for the
        # same index (make it deterministic per index), but don't mess-up
        # RNG state outside this method.

        # ====== YOUR CODE: ======

        img_tensor = torch.rand(*self.image_dim)
        return img_tensor, random.randint(0, self.num_classes)
        # ========================

    def __len__(self):
        # ====== YOUR CODE: ======
        raise NotImplementedError()
        # ========================


class SubsetDataset(Dataset):
    """
    A dataset that wraps another dataset, returning a subset from it.
    """

    def __init__(self, source_dataset: Dataset, subset_len, offset=0):
        """
        Create a SubsetDataset from another dataset.
        :param source_dataset: The dataset to take samples from.
        :param subset_len: The total number of sample in the subset.
        :param offset: The offset index to start taking samples from.
        """
        if offset + subset_len > len(source_dataset):
            raise ValueError("Not enough samples in source dataset")

        self.source_dataset = source_dataset
        self.subset_len = subset_len
        self.offset = offset

    def __getitem__(self, index):
        # TODO: Return the item at index + offset from the source dataset.
        # Make sure to raise an IndexError if index is out of bounds.

        # ====== YOUR CODE: ======
        raise NotImplementedError()
        # ========================

    def __len__(self):
        # ====== YOUR CODE: ======
        raise NotImplementedError()
        # ========================


if __name__ == '__main__':
    # Create the dataset
    num_samples = 1000
    num_classes = 10
    image_size = (3, 32, 32)
    ds = hw1datasets.RandomImageDataset(num_samples, num_classes, *image_size)

    # You can load individual items from the dataset by indexing
    img0, cls0 = ds[0]

    # Plot first N images from the dataset with a helper function
    fig, axes = plot.dataset_first_n(ds, 9, show_classes=True, nrows=3)
    fig.show()