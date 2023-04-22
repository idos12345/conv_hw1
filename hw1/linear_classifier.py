from typing import Tuple

import torch
from torch import Tensor
from torch.utils.data import DataLoader
from collections import namedtuple

from .losses import ClassifierLoss


class LinearClassifier:
    def __init__(self, n_features: int, n_classes: int, weight_std: float = 0.001):
        """
        Initializes the linear classifier.
        :param n_features: Number or features in each sample.
        :param n_classes: Number of classes samples can belong to.
        :param weight_std: Standard deviation of initial weights.
        """
        self.n_features = n_features
        self.n_classes = n_classes

        # TODO: Create weights tensor of appropriate dimensions
        # Initialize it from a normal dist with zero mean and the given std.

        self.weights = None
        # ====== YOUR CODE: ======
        self.weights = torch.normal(0, weight_std, size=(n_features, n_classes))
        # ========================

    def predict(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        """
        Predict the class of a batch of samples based on the current weights.
        :param x: A tensor of shape (N,n_features) where N is the batch size.
        :return:
            y_pred: Tensor of shape (N,) where each entry is the predicted
                class of the corresponding sample. Predictions are integers in
                range [0, n_classes-1].
            class_scores: Tensor of shape (N,n_classes) with the class score
                per sample.
        """

        # TODO: Implement linear prediction.
        # Calculate the score for each class using the weights and
        # return the class y_pred with the highest score.

        y_pred, class_scores = None, None
        # ====== YOUR CODE: ======
        class_scores = torch.mm(x, self.weights)
        y_pred = torch.argmax(class_scores, dim=1)
        # ========================

        return y_pred, class_scores

    @staticmethod
    def evaluate_accuracy(y: Tensor, y_pred: Tensor) -> float:
        """
        Calculates the prediction accuracy based on predicted and ground-truth
        labels.
        :param y: A tensor of shape (N,) containing ground truth class labels.
        :param y_pred: A tensor of shape (N,) containing predicted labels.
        :return: The accuracy in percent.
        """

        # TODO: calculate accuracy of prediction.
        # Use the predict function above and compare the predicted class
        # labels to the ground truth labels to obtain the accuracy (in %).
        # Do not use an explicit loop.

        acc = None
        # ====== YOUR CODE: ======
        acc = torch.sum(y == y_pred) / y.size(0)
        # ========================

        return acc * 100

    def train(
            self,
            dl_train: DataLoader,
            dl_valid: DataLoader,
            loss_fn: ClassifierLoss,
            learn_rate: float = 0.1,
            weight_decay: float = 0.001,
            max_epochs: int = 100,
    ):

        Result = namedtuple('Result', 'accuracy loss')
        train_res = Result(accuracy=[], loss=[])
        valid_res = Result(accuracy=[], loss=[])

        print('Training', end='')
        for epoch_idx in range(max_epochs):

            # TODO: Implement model training loop.
            # At each epoch, evaluate the model on the entire training set
            # (batch by batch) and update the weights.
            # Each epoch, also evaluate on the validation set.
            # Accumulate average loss and total accuracy for both sets.
            # The train/valid_res variables should hold the average loss and
            # accuracy per epoch.
            #
            # Don't forget to add a regularization term to the loss, using the
            # weight_decay parameter.

            total_correct = 0
            average_loss = 0

            # ====== YOUR CODE: ======
            for data, labels in dl_train:
                pred, scores = self.predict(data)
                W = self.weights
                loss = loss_fn.loss(data, labels, scores, pred) + (weight_decay/2) * torch.sum(W ** 2)
                grad = loss_fn.grad() + weight_decay * W
                self.weights = W - learn_rate * grad
                average_loss += loss
                total_correct += self.evaluate_accuracy(labels, pred)
            train_res.accuracy.append(total_correct / len(dl_train))
            train_res.loss.append(average_loss / len(dl_train))

            total_correct = 0
            average_loss = 0
            for data, labels in dl_valid:
                pred, scores = self.predict(data)
                loss = loss_fn.loss(data, labels, scores, pred) + (weight_decay/2) * torch.sum(W * W)
                average_loss += loss
                total_correct += self.evaluate_accuracy(labels, pred)
            valid_res.accuracy.append(total_correct / len(dl_valid))
            valid_res.loss.append(average_loss / len(dl_valid))
            # ========================
            print('.', end='')

        print('')
        return train_res, valid_res

    def weights_as_images(self, img_shape, has_bias=True):
        """
        Create tensor images from the weights, for visualization.
        :param img_shape: Shape of each tensor image to create, i.e. (C,H,W).
        :param has_bias: Whether the weights include a bias component
            (assumed to be at the end).
        :return: Tensor of shape (n_classes, C, H, W).
        """

        # TODO: Convert the weights matrix into a tensor of images.
        # The output shape should be (n_classes, C, H, W).

        # ====== YOUR CODE: ======
        W = self.weights
        if has_bias:
            W = W[:-1]
        w_images = W.T.reshape((self.n_classes, ) + img_shape)
        # ========================

        return w_images
