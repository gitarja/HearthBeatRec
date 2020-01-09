import pandas as pd
import glob
import os
import random


class ImageGenerator():
    def __init__(self, path=None):
        # QThread.__init__(self)
        self.data = pd.read_csv(path)
        self.data = self.data.sample(frac=1)
        self.imageList = []
        # self.criteria = [["N"], ["LM", "LM"], ["N"], ["LM", "MH"], ["N"], ["MH", "LM"], ["N"], ["MH", "MH"]]
        self.criteria = [["LM", "LM"], ["LM", "MH"], ["MH", "LM"], ["MH", "MH"]]
        self.i = 0
        self.iP = 0

    def setParams(self, sex):
        self.sex = sex
        if sex == "M":
            self.valence = "Valence_label_men"
            self.arousal = "Arousal_label_men"
        else:
            self.valence = "Valence_label_women"
            self.arousal = "Arousal_label_women"

    def pickImage(self):
        image = self.getImage()
        self.i += 1
        if (self.i > 3):
            self.i = 0

        return image["Images"], image[self.valence], image[self.arousal], image["GIF"]

    def getImage(self):
        currentStep = self.criteria[self.i]
        candidates = self.data.loc[~self.data["Images"].isin(self.imageList)]
        # candidates = candidates.sample(frac=1.)

        imageCandidates = candidates[
            (candidates[self.valence] == currentStep[0]) & (candidates[self.arousal] == currentStep[1]) & (
                    candidates["Type"] != "P") & (
                    candidates["Type"] != self.sex)]
        # print(random.randint(1, 2))
        # To select sad
        if (self.i == 0):
            imageCandidatesG = candidates[candidates["Type"] == "S"]
            if (len(imageCandidatesG) != 0):
                imageCandidates = imageCandidatesG
        #To select accident
        if (self.i == 1 and random.randint(1, 2) == 2):
            imageCandidatesG = candidates[candidates["Type"] == "A"]
            if (len(imageCandidatesG) != 0):
                imageCandidates = imageCandidatesG
        # To select relaxed gif
        if (self.i == 2 and random.randint(1, 2) == 2):
            imageCandidatesG = candidates[candidates["Type"] == "R"]
            if (len(imageCandidatesG) != 0):
                imageCandidates = imageCandidatesG
        #To select funny gif
        if (self.i == 3):
            imageCandidatesD = candidates[candidates["Type"] == "D"]
            if (len(imageCandidatesD) != 0):
                imageCandidates = imageCandidatesD
            else:
                imageCandidatesD = candidates[candidates["Type"] == "H"]
                if (len(imageCandidatesD) != 0):
                    imageCandidates = imageCandidatesD

        if (len(imageCandidates) == 0):
            imageCandidates = candidates
        imageCandidates = imageCandidates.sample(frac=1)
        image = imageCandidates.iloc[random.randint(0, len(imageCandidates) - 1)]
        self.imageList.append(image["Images"])
        return image

    def pickImagePersonal(self):
        personal = False
        valLabel = "MH"
        arLabel = "MH"
        if (self.i <= 3):
            data = self.getImage()
            image = data["Images"]
            valLabel = data[self.valence]
            arLabel = data[self.arousal]
            GIF = data["GIF"]

        elif (self.i == 4):
            image = os.path.basename(self.personalImage.iloc[self.iP]["Images"])
            self.imageList.append(image)
            personal = True
            valLabel = "MH"
            arLabel = "MH"
            self.iP += 1
            GIF = 0
        self.i += 1

        if (self.i > 4):
            self.i = 0

        return image, valLabel, arLabel, personal, GIF

    def readPersonalPictures(self, path):
        types = ('*.jpg', '*.png', '*.jpeg')  # the tuple of file types
        filesGrabbed = []
        for files in types:
            filesGrabbed.extend(glob.glob(os.path.join(path, files)))

        self.personalImage = pd.DataFrame(filesGrabbed, columns=["Images"])
        self.personalImage = self.personalImage.sample(frac=1.)

        return len(self.personalImage.index)
