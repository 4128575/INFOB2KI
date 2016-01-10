# mira.py
# -------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Mira implementation
import util
PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.legalLabels = legalLabels
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        self.features = trainingData[0].keys() # this could be useful for your code later...

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        """
        This method sets self.weights using MIRA.  Train the classifier for each value of C in Cgrid,
        then store the weights that give the best accuracy on the validationData.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        representing a vector of values.
        """

        tempWeights = util.Counter()
        """The implementation is fairly similar to the one in perceptron.py. We have to loop through the
        iterations ourselves and the weight updating is different."""
        for c in Cgrid:
            tempWeights[c] = self.weights.copy()
            for i in range(self.max_iterations):
                for i in range(len(trainingData)):
                    "Initiation"
                    currentDatum = trainingData[i]
                    referenceLabel = trainingLabels[i]
                    currentScore = util.Counter()

                    "We calculate the scores similarly to perceptron.py."
                    for label in self.legalLabels:
                        currentScore[label] = currentDatum * tempWeights[c][label]

                    "We pick the best score."
                    currentLabel = currentScore.argMax()

                    "If the instance is not correct, we update the weights via the MIRA method."
                    if currentLabel != referenceLabel:
                        tempDatum = currentDatum.copy()
                        for datum in tempDatum:
                            tempDatum[datum] = tempDatum[datum] * tempDatum[datum]

                        "We calculate tau as prescribed on the Berkeley site."
                        tempTau = ((tempWeights[c][currentLabel] - tempWeights[c][referenceLabel]) * currentDatum + 1.0) / (2 * tempDatum.totalCount())
                        tau = min(c, tempTau)
                        tempDatum2 = currentDatum.copy()
                        for k in tempDatum2:
                            tempDatum2[k] = tempDatum2[k] * tau

                        "We update the weights."
                        tempWeights[c][currentLabel] = tempWeights[c][currentLabel] - tempDatum2
                        tempWeights[c][referenceLabel] = tempWeights[c][referenceLabel] + tempDatum2

        "Now we have to find the best C value. First we define the best C and the accuracy."
        cValue = Cgrid[0]
        accuracy = 0
        for c in Cgrid:
            correctGuesses = 0

            "Since the classify method uses self.weights we need to set it to tempWeights here."
            self.weights = tempWeights[c]
            guessList = self.classify(validationData)
            validationIndex = 0
            for guess in guessList:
                if guess == validationLabels[validationIndex]:
                    correctGuesses += 1
                validationIndex += 1

            "We determine the accuracy for this particular C value."
            tempAcc = correctGuesses / len(validationData)
            if tempAcc > accuracy:
                accuracy = tempAcc
                cValue = c
            if tempAcc == accuracy:
                cValue = min(cValue, c)

        self.weights = tempWeights[cValue]

    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


