"""
Download, transform and simulate various datasets.
"""

# Author: Georgios Douzas <gdouzas@icloud.com>
#         Joao Fonseca <jpmrfonseca@gmail.com>
# License: MIT

from os.path import join
from re import sub
from collections import Counter
from itertools import product
from urllib.parse import urljoin
from string import ascii_lowercase
from zipfile import ZipFile
from io import BytesIO, StringIO
from sqlite3 import connect
from scipy.io import loadmat
import io

from rich.progress import track
import requests
import numpy as np
import pandas as pd
from sklearn.utils import check_X_y
from imblearn.datasets import make_imbalance

from research.utils import img_array_to_pandas

UCI_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/"
KEEL_URL = "http://sci2s.ugr.es/keel/keel-dataset/datasets/imbalanced/"
GIC_URL = "http://www.ehu.eus/ccwintco/uploads/"
OPENML_URL = "https://www.openml.org/data/get_csv/"
FETCH_URLS = {
    "breast_tissue": urljoin(UCI_URL, "00192/BreastTissue.xls"),
    "ecoli": urljoin(UCI_URL, "ecoli/ecoli.data"),
    "eucalyptus": urljoin(OPENML_URL, "3625/dataset_194_eucalyptus.arff"),
    "glass": urljoin(UCI_URL, "glass/glass.data"),
    "haberman": urljoin(UCI_URL, "haberman/haberman.data"),
    "heart": urljoin(UCI_URL, "statlog/heart/heart.dat"),
    "iris": urljoin(UCI_URL, "iris/bezdekIris.data"),
    "libras": urljoin(UCI_URL, "libras/movement_libras.data"),
    "liver": urljoin(UCI_URL, "liver-disorders/bupa.data"),
    "pima": "https://gist.githubusercontent.com/ktisha/c21e73a1bd1700294ef790c56c8aec1f"
    "/raw/819b69b5736821ccee93d05b51de0510bea00294/pima-indians-diabetes.csv",
    "vehicle": urljoin(UCI_URL, "statlog/vehicle/"),
    "wine": urljoin(UCI_URL, "wine/wine.data"),
    "new_thyroid_1": urljoin(
        urljoin(KEEL_URL, "imb_IRlowerThan9/"), "new-thyroid1.zip"
    ),
    "new_thyroid_2": urljoin(
        urljoin(KEEL_URL, "imb_IRlowerThan9/"), "new-thyroid2.zip"
    ),
    "cleveland": urljoin(
        urljoin(KEEL_URL, "imb_IRhigherThan9p2/"), "cleveland-0_vs_4.zip"
    ),
    "led": urljoin(
        urljoin(KEEL_URL, "imb_IRhigherThan9p2/"), "led7digit-0-2-4-5-6-7-8-9_vs_1.zip"
    ),
    "page_blocks_1_3": urljoin(
        urljoin(KEEL_URL, "imb_IRhigherThan9p1/"), "page-blocks-1-3_vs_4.zip"
    ),
    "vowel": urljoin(urljoin(KEEL_URL, "imb_IRhigherThan9p1/"), "vowel0.zip"),
    "yeast_1": urljoin(urljoin(KEEL_URL, "imb_IRlowerThan9/"), "yeast1.zip"),
    "banknote_authentication": urljoin(
        UCI_URL, "00267/data_banknote_authentication.txt"
    ),
    "arcene": urljoin(UCI_URL, "arcene/"),
    "audit": urljoin(UCI_URL, "00475/audit_data.zip"),
    "spambase": urljoin(UCI_URL, "spambase/spambase.data"),
    "parkinsons": urljoin(UCI_URL, "parkinsons/parkinsons.data"),
    "ionosphere": urljoin(UCI_URL, "ionosphere/ionosphere.data"),
    "breast_cancer": urljoin(UCI_URL, "breast-cancer-wisconsin/wdbc.data"),
    "adult": urljoin(UCI_URL, "adult/adult.data"),
    "abalone": urljoin(UCI_URL, "abalone/abalone.data"),
    "acute": urljoin(UCI_URL, "acute/diagnosis.data"),
    "annealing": urljoin(UCI_URL, "annealing/anneal.data"),
    "census": urljoin(UCI_URL, "census-income-mld/census-income.data.gz"),
    "contraceptive": urljoin(UCI_URL, "cmc/cmc.data"),
    "covertype": urljoin(UCI_URL, "covtype/covtype.data.gz"),
    "credit_approval": urljoin(UCI_URL, "credit-screening/crx.data"),
    "dermatology": urljoin(UCI_URL, "dermatology/dermatology.data"),
    "echocardiogram": urljoin(UCI_URL, "echocardiogram/echocardiogram.data"),
    "flags": urljoin(UCI_URL, "flags/flag.data"),
    "heart_disease": [
        urljoin(UCI_URL, "heart-disease/processed.cleveland.data"),
        urljoin(UCI_URL, "heart-disease/processed.hungarian.data"),
        urljoin(UCI_URL, "heart-disease/processed.switzerland.data"),
        urljoin(UCI_URL, "heart-disease/processed.va.data"),
    ],
    "hepatitis": urljoin(UCI_URL, "hepatitis/hepatitis.data"),
    "german_credit": urljoin(UCI_URL, "statlog/german/german.data"),
    "thyroid": urljoin(UCI_URL, "thyroid-disease/thyroid0387.data"),
    "first_order_theorem": urljoin(OPENML_URL, "1587932/phpPbCMyg"),
    "gas_drift": urljoin(OPENML_URL, "1588715/phpbL6t4U"),
    "autouniv_au7": urljoin(OPENML_URL, "1593748/phpmRPvKy"),
    "autouniv_au4": urljoin(OPENML_URL, "1593744/phpiubDlf"),
    "mice_protein": urljoin(OPENML_URL, "17928620/phpchCuL5"),
    "steel_plates": urljoin(OPENML_URL, "18151921/php5s7Ep8"),
    "cardiotocography": urljoin(OPENML_URL, "1593756/phpW0AXSQ"),
    "waveform": urljoin(OPENML_URL, "60/dataset_60_waveform-5000.arff"),
    "volkert": urljoin(OPENML_URL, "19335689/file1c556e3db171.arff"),
    "asp_potassco": urljoin(OPENML_URL, "21377447/file18547f421393.arff"),
    "wine_quality": urljoin(OPENML_URL, "4965268/wine-quality-red.arff"),
    "mfeat_zernike": urljoin(OPENML_URL, "22/dataset_22_mfeat-zernike.arff"),
    "gesture_segmentation": urljoin(OPENML_URL, "1798765/phpYLeydd"),
    "texture": urljoin(OPENML_URL, "4535764/phpBDgUyY"),
    "usps": urljoin(OPENML_URL, "19329737/usps.arff"),
    "japanese_vowels": urljoin(OPENML_URL, "52415/JapaneseVowels.arff"),
    "pendigits": urljoin(OPENML_URL, "32/dataset_32_pendigits.arff"),
    "image_segmentation": urljoin(OPENML_URL, "18151937/phpyM5ND4"),
    "baseball": urljoin(OPENML_URL, "3622/dataset_189_baseball.arff"),
    "indian_pines": [
        urljoin(GIC_URL, "2/22/Indian_pines.mat"),
        urljoin(GIC_URL, "c/c4/Indian_pines_gt.mat"),
    ],
    "salinas": [
        urljoin(GIC_URL, "f/f1/Salinas.mat"),
        urljoin(GIC_URL, "f/fa/Salinas_gt.mat"),
    ],
    "salinas_a": [
        urljoin(GIC_URL, "d/df/SalinasA.mat"),
        urljoin(GIC_URL, "a/aa/SalinasA_gt.mat"),
    ],
    "pavia_centre": [
        urljoin(GIC_URL, "e/e3/Pavia.mat"),
        urljoin(GIC_URL, "5/53/Pavia_gt.mat"),
    ],
    "pavia_university": [
        urljoin(GIC_URL, "e/ee/PaviaU.mat"),
        urljoin(GIC_URL, "5/50/PaviaU_gt.mat"),
    ],
    "kennedy_space_center": [
        urljoin(GIC_URL, "2/26/KSC.mat"),
        urljoin(GIC_URL, "a/a6/KSC_gt.mat"),
    ],
    "botswana": [
        urljoin(GIC_URL, "7/72/Botswana.mat"),
        urljoin(GIC_URL, "5/58/Botswana_gt.mat"),
    ],
}
RANDOM_STATE = 0


class Datasets:
    """Base class to download and save datasets."""

    def __init__(self, names="all"):
        self.names = names

    @staticmethod
    def _modify_columns(data):
        """Rename and reorder columns of dataframe."""
        X, y = data.drop(columns="target"), data.target
        X.columns = range(len(X.columns))
        return pd.concat([X, y], axis=1)

    def download(self):
        """Download the datasets."""
        if self.names == "all":
            func_names = [func_name for func_name in dir(self) if "fetch_" in func_name]
        else:
            func_names = [
                f"fetch_{name}".lower().replace(" ", "_") for name in self.names
            ]
        self.content_ = []
        for func_name in track(func_names, description="Datasets"):
            name = func_name.replace("fetch_", "").upper().replace("_", " ")
            fetch_data = getattr(self, func_name)
            data = self._modify_columns(fetch_data())
            self.content_.append((name, data))
        return self

    def save(self, path, db_name):
        """Save datasets."""
        with connect(join(path, f"{db_name}.db")) as connection:
            for name, data in self.content_:
                data.to_sql(name, connection, index=False, if_exists="replace")


class ImbalancedBinaryDatasets(Datasets):
    """Class to download, transform and save binary class imbalanced
    datasets."""

    MULTIPLICATION_FACTORS = [2, 3]

    @staticmethod
    def _calculate_ratio(multiplication_factor, y):
        """Calculate ratio based on IRs multiplication factor."""
        ratio = Counter(y).copy()
        ratio[1] = int(ratio[1] / multiplication_factor)
        return ratio

    def _make_imbalance(self, data, multiplication_factor):
        """Undersample the minority class."""
        X_columns = [col for col in data.columns if col != "target"]
        X, y = check_X_y(data.loc[:, X_columns], data.target)
        if multiplication_factor > 1.0:
            sampling_strategy = self._calculate_ratio(multiplication_factor, y)
            X, y = make_imbalance(
                X, y, sampling_strategy=sampling_strategy, random_state=RANDOM_STATE
            )
        data = pd.DataFrame(np.column_stack((X, y)))
        data.iloc[:, -1] = data.iloc[:, -1].astype(int)
        return data

    def download(self):
        """Download the datasets and append undersampled versions of them."""
        super(ImbalancedBinaryDatasets, self).download()
        undersampled_datasets = []
        for (name, data), factor in list(
            product(self.content_, self.MULTIPLICATION_FACTORS)
        ):
            ratio = self._calculate_ratio(factor, data.target)
            if ratio[1] >= 15:
                data = self._make_imbalance(data, factor)
                undersampled_datasets.append((f"{name} ({factor})", data))
        self.content_ += undersampled_datasets
        return self

    def fetch_breast_tissue(self):
        """Download and transform the Breast Tissue Data Set.
        The minority class is identified as the `car` and `fad`
        labels and the majority class as the rest of the labels.

        http://archive.ics.uci.edu/ml/datasets/breast+tissue
        """
        data = pd.read_excel(FETCH_URLS["breast_tissue"], sheet_name="Data")
        data = data.drop(columns="Case #").rename(columns={"Class": "target"})
        data["target"] = data["target"].isin(["car", "fad"]).astype(int)
        return data

    def fetch_ecoli(self):
        """Download and transform the Ecoli Data Set.
        The minority class is identified as the `pp` label
        and the majority class as the rest of the labels.

        https://archive.ics.uci.edu/ml/datasets/ecoli
        """
        data = pd.read_csv(FETCH_URLS["ecoli"], header=None, delim_whitespace=True)
        data = data.drop(columns=0).rename(columns={8: "target"})
        data["target"] = data["target"].isin(["pp"]).astype(int)
        return data

    def fetch_eucalyptus(self):
        """Download and transform the Eucalyptus Data Set.
        The minority class is identified as the `best` label
        and the majority class as the rest of the labels.

        https://www.openml.org/d/188
        """
        data = pd.read_csv(FETCH_URLS["eucalyptus"])
        data = data.iloc[:, -9:].rename(columns={"Utility": "target"})
        data = data[data != "?"].dropna()
        data["target"] = data["target"].isin(["best"]).astype(int)
        return data

    def fetch_glass(self):
        """Download and transform the Glass Identification Data Set.
        The minority class is identified as the `1` label
        and the majority class as the rest of the labels.

        https://archive.ics.uci.edu/ml/datasets/glass+identification
        """
        data = pd.read_csv(FETCH_URLS["glass"], header=None)
        data = data.drop(columns=0).rename(columns={10: "target"})
        data["target"] = data["target"].isin([1]).astype(int)
        return data

    def fetch_haberman(self):
        """Download and transform the Haberman's Survival Data Set.
        The minority class is identified as the `1` label
        and the majority class as the `0` label.

        https://archive.ics.uci.edu/ml/datasets/Haberman's+Survival
        """
        data = pd.read_csv(FETCH_URLS["haberman"], header=None)
        data.rename(columns={3: "target"}, inplace=True)
        data["target"] = data["target"].isin([2]).astype(int)
        return data

    def fetch_heart(self):
        """Download and transform the Heart Data Set.
        The minority class is identified as the `2` label
        and the majority class as the `1` label.

        http://archive.ics.uci.edu/ml/datasets/statlog+(heart)
        """
        data = pd.read_csv(FETCH_URLS["heart"], header=None, delim_whitespace=True)
        data.rename(columns={13: "target"}, inplace=True)
        data["target"] = data["target"].isin([2]).astype(int)
        return data

    def fetch_iris(self):
        """Download and transform the Iris Data Set.
        The minority class is identified as the `1` label
        and the majority class as the rest of the labels.

        https://archive.ics.uci.edu/ml/datasets/iris
        """
        data = pd.read_csv(FETCH_URLS["iris"], header=None)
        data.rename(columns={4: "target"}, inplace=True)
        data["target"] = data["target"].isin(["Iris-setosa"]).astype(int)
        return data

    def fetch_libras(self):
        """Download and transform the Libras Movement Data Set.
        The minority class is identified as the `1` label
        and the majority class as the rest of the labels.

        https://archive.ics.uci.edu/ml/datasets/Libras+Movement
        """
        data = pd.read_csv(FETCH_URLS["libras"], header=None)
        data.rename(columns={90: "target"}, inplace=True)
        data["target"] = data["target"].isin([1]).astype(int)
        return data

    def fetch_liver(self):
        """Download and transform the Liver Disorders Data Set.
        The minority class is identified as the `1` label
        and the majority class as the '2' label.

        https://archive.ics.uci.edu/ml/datasets/liver+disorders
        """
        data = pd.read_csv(FETCH_URLS["liver"], header=None)
        data.rename(columns={6: "target"}, inplace=True)
        data["target"] = data["target"].isin([1]).astype(int)
        return data

    def fetch_pima(self):
        """Download and transform the Pima Indians Diabetes Data Set.
        The minority class is identified as the `1` label
        and the majority class as the '0' label.

        https://www.kaggle.com/uciml/pima-indians-diabetes-database
        """
        data = pd.read_csv(FETCH_URLS["pima"], header=None, skiprows=9)
        data.rename(columns={8: "target"}, inplace=True)
        return data

    def fetch_vehicle(self):
        """Download and transform the Vehicle Silhouettes Data Set.
        The minority class is identified as the `1` label
        and the majority class as the rest of the labels.

        https://archive.ics.uci.edu/ml/datasets/Statlog+(Vehicle+Silhouettes)
        """
        data = pd.DataFrame()
        for letter in ascii_lowercase[0:9]:
            partial_data = pd.read_csv(
                urljoin(FETCH_URLS["vehicle"], "xa%s.dat" % letter),
                header=None,
                delim_whitespace=True,
            )
            partial_data = partial_data.rename(columns={18: "target"})
            partial_data["target"] = partial_data["target"].isin(["van"]).astype(int)
            data = data.append(partial_data)
        return data

    def fetch_wine(self):
        """Download and transform the Wine Data Set.
        The minority class is identified as the `2` label
        and the majority class as the rest of the labels.

        https://archive.ics.uci.edu/ml/datasets/wine
        """
        data = pd.read_csv(FETCH_URLS["wine"], header=None)
        data.rename(columns={0: "target"}, inplace=True)
        data["target"] = data["target"].isin([2]).astype(int)
        return data

    def fetch_new_thyroid_1(self):
        """Download and transform the Thyroid 1 Disease Data Set.
        The minority class is identified as the `positive`
        label and the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=145
        """
        zipped_data = requests.get(FETCH_URLS["new_thyroid_1"]).content
        unzipped_data = (
            ZipFile(BytesIO(zipped_data)).read("new-thyroid1.dat").decode("utf-8")
        )
        data = pd.read_csv(
            StringIO(sub(r"@.+\n+", "", unzipped_data)),
            header=None,
            sep=", ",
            engine="python",
        )
        data.rename(columns={5: "target"}, inplace=True)
        data["target"] = data["target"].isin(["positive"]).astype(int)
        return data

    def fetch_new_thyroid_2(self):
        """Download and transform the Thyroid 2 Disease Data Set.
        The minority class is identified as the `positive`
        label and the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=146
        """
        zipped_data = requests.get(FETCH_URLS["new_thyroid_2"]).content
        unzipped_data = (
            ZipFile(BytesIO(zipped_data)).read("newthyroid2.dat").decode("utf-8")
        )
        data = pd.read_csv(
            StringIO(sub(r"@.+\n+", "", unzipped_data)),
            header=None,
            sep=", ",
            engine="python",
        )
        data.rename(columns={5: "target"}, inplace=True)
        data["target"] = data["target"].isin(["positive"]).astype(int)
        return data

    def fetch_cleveland(self):
        """Download and transform the Heart Disease Cleveland Data Set.
        The minority class is identified as the `positive` label and
        the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=980
        """
        zipped_data = requests.get(FETCH_URLS["cleveland"]).content
        unzipped_data = (
            ZipFile(BytesIO(zipped_data)).read("cleveland-0_vs_4.dat").decode("utf-8")
        )
        data = pd.read_csv(StringIO(sub(r"@.+\n+", "", unzipped_data)), header=None)
        data.rename(columns={13: "target"}, inplace=True)
        data["target"] = data["target"].isin(["positive"]).astype(int)
        return data

    def fetch_dermatology(self):
        """Download and transform the Dermatology Data Set.
        The minority class is identified as the `positive` label and
        the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=1330
        """
        data = pd.read_csv(FETCH_URLS["dermatology"], header=None)
        data.rename(columns={34: "target"}, inplace=True)
        data.drop(columns=33, inplace=True)
        data["target"] = data["target"].isin(["positive"]).astype(int)
        return data

    def fetch_led(self):
        """Download and transform the LED Display Domain Data Set.
        The minority class is identified as the `positive` label and
        the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=998
        """
        zipped_data = requests.get(FETCH_URLS["led"]).content
        unzipped_data = (
            ZipFile(BytesIO(zipped_data))
            .read("led7digit-0-2-4-5-6-7-8-9_vs_1.dat")
            .decode("utf-8")
        )
        data = pd.read_csv(StringIO(sub(r"@.+\n+", "", unzipped_data)), header=None)
        data.rename(columns={7: "target"}, inplace=True)
        data["target"] = data["target"].isin(["positive"]).astype(int)
        return data

    def fetch_page_blocks_1_3(self):
        """Download and transform the Page Blocks 1-3 Data Set.
        The minority class is identified as the `positive` label and
        the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=124
        """
        zipped_data = requests.get(FETCH_URLS["page_blocks_1_3"]).content
        unzipped_data = (
            ZipFile(BytesIO(zipped_data))
            .read("page-blocks-1-3_vs_4.dat")
            .decode("utf-8")
        )
        data = pd.read_csv(StringIO(sub(r"@.+\n+", "", unzipped_data)), header=None)
        data.rename(columns={10: "target"}, inplace=True)
        data["target"] = data["target"].isin(["positive"]).astype(int)
        return data

    def fetch_vowel(self):
        """Download and transform the Vowel Recognition Data Set.
        The minority class is identified as the `positive` label and
        the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=127
        """
        zipped_data = requests.get(FETCH_URLS["vowel"]).content
        unzipped_data = ZipFile(BytesIO(zipped_data)).read("vowel0.dat").decode("utf-8")
        data = pd.read_csv(StringIO(sub(r"@.+\n+", "", unzipped_data)), header=None)
        data.rename(columns={13: "target"}, inplace=True)
        data["target"] = data["target"].isin([" positive"]).astype(int)
        return data

    def fetch_yeast_1(self):
        """Download and transform the Yeast 1 Data Set.
        The minority class is identified as the `positive` label and
        the majority class as the `negative` label.

        http://sci2s.ugr.es/keel/dataset.php?cod=153
        """
        zipped_data = requests.get(FETCH_URLS["yeast_1"]).content
        unzipped_data = ZipFile(BytesIO(zipped_data)).read("yeast1.dat").decode("utf-8")
        data = pd.read_csv(StringIO(sub(r"@.+\n+", "", unzipped_data)), header=None)
        data.rename(columns={8: "target"}, inplace=True)
        data["target"] = data["target"].isin([" positive"]).astype(int)
        return data


class BinaryDatasets(Datasets):
    """Class to download, transform and save binary class datasets."""

    def fetch_banknote_authentication(self):
        """Download and transform the Banknote Authentication Data Set.

        https://archive.ics.uci.edu/ml/datasets/banknote+authentication
        """
        data = pd.read_csv(FETCH_URLS["banknote_authentication"], header=None)
        data.rename(columns={4: "target"}, inplace=True)
        return data

    def fetch_arcene(self):
        """Download and transform the Arcene Data Set.

        https://archive.ics.uci.edu/ml/datasets/Arcene
        """
        url = FETCH_URLS["arcene"]
        data, labels = [], []
        for data_type in ("train", "valid"):
            data.append(
                pd.read_csv(
                    urljoin(url, f"ARCENE/arcene_{data_type}.data"),
                    header=None,
                    sep=" ",
                ).drop(columns=list(range(1998, 10001)))
            )
            labels.append(
                pd.read_csv(
                    urljoin(
                        url,
                        ("ARCENE/" if data_type == "train" else "")
                        + f"arcene_{data_type}.labels",
                    ),
                    header=None,
                ).rename(columns={0: "target"})
            )
        data = pd.concat(data, ignore_index=True)
        labels = pd.concat(labels, ignore_index=True)
        data = pd.concat([data, labels], axis=1)
        data["target"] = data["target"].isin([1]).astype(int)
        return data

    def fetch_audit(self):
        """Download and transform the Audit Data Set.

        https://archive.ics.uci.edu/ml/datasets/Audit+Data
        """
        zipped_data = requests.get(FETCH_URLS["audit"]).content
        unzipped_data = (
            ZipFile(BytesIO(zipped_data))
            .read("audit_data/audit_risk.csv")
            .decode("utf-8")
        )
        data = pd.read_csv(StringIO(sub(r"@.+\n+", "", unzipped_data)), engine="python")
        data = (
            data.drop(columns=["LOCATION_ID"])
            .rename(columns={"Risk": "target"})
            .dropna()
        )
        return data

    def fetch_spambase(self):
        """Download and transform the Spambase Data Set.

        https://archive.ics.uci.edu/ml/datasets/Spambase
        """
        data = pd.read_csv(FETCH_URLS["spambase"], header=None)
        data.rename(columns={57: "target"}, inplace=True)
        return data

    def fetch_parkinsons(self):
        """Download and transform the Parkinsons Data Set.

        https://archive.ics.uci.edu/ml/datasets/parkinsons
        """
        data = pd.read_csv(FETCH_URLS["parkinsons"])
        data = pd.concat(
            [
                data.drop(columns=["name", "status"]),
                data[["status"]].rename(columns={"status": "target"}),
            ],
            axis=1,
        )
        data["target"] = data["target"].isin([0]).astype(int)
        return data

    def fetch_ionosphere(self):
        """Download and transform the Ionosphere Data Set.

        https://archive.ics.uci.edu/ml/datasets/ionosphere
        """
        data = pd.read_csv(FETCH_URLS["ionosphere"], header=None)
        data = data.drop(columns=[0, 1]).rename(columns={34: "target"})
        data["target"] = data["target"].isin(["b"]).astype(int)
        return data

    def fetch_breast_cancer(self):
        """Download and transform the Breast Cancer Wisconsin Data Set.

        https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
        """
        data = pd.read_csv(FETCH_URLS["breast_cancer"], header=None)
        data = pd.concat(
            [data.drop(columns=[0, 1]), data[[1]].rename(columns={1: "target"})], axis=1
        )
        data["target"] = data["target"].isin(["M"]).astype(int)
        return data


class ContinuousCategoricalDatasets(Datasets):
    """Class to download, transform and save datasets with both continuous
    and categorical features."""

    @staticmethod
    def _modify_columns(data, categorical_features):
        """Rename and reorder columns of dataframe."""
        X, y = data.drop(columns="target"), data.target
        X.columns = range(len(X.columns))
        return pd.concat([X, y], axis=1), categorical_features

    def download(self):
        """Download the datasets."""
        if self.names == "all":
            func_names = [func_name for func_name in dir(self) if "fetch_" in func_name]
        else:
            func_names = [
                f"fetch_{name}".lower().replace(" ", "_") for name in self.names
            ]
        self.content_ = []
        for func_name in track(func_names, description="Datasets"):
            name = func_name.replace("fetch_", "").upper().replace("_", " ")
            fetch_data = getattr(self, func_name)
            data, categorical_features = self._modify_columns(*fetch_data())
            self.content_.append((name, data, categorical_features))
        return self

    def save(self, path, db_name):
        """Save datasets."""
        with connect(join(path, f"{db_name}.db")) as connection:
            for name, data in self.content_:
                data.to_sql(name, connection, index=False, if_exists="replace")

    def fetch_adult(self):
        """Download and transform the Adult Data Set.

        https://archive.ics.uci.edu/ml/datasets/Adult
        """
        data = pd.read_csv(FETCH_URLS["adult"], header=None, na_values=" ?").dropna()
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [1, 3, 5, 6, 7, 8, 9, 13]
        return data, categorical_features

    def fetch_abalone(self):
        """Download and transform the Abalone Data Set.

        https://archive.ics.uci.edu/ml/datasets/Abalone
        """
        data = pd.read_csv(FETCH_URLS["abalone"], header=None)
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [0]
        return data, categorical_features

    def fetch_acute(self):
        """Download and transform the Acute Inflammations Data Set.

        https://archive.ics.uci.edu/ml/datasets/Acute+Inflammations
        """
        data = pd.read_csv(
            FETCH_URLS["acute"], header=None, sep="\t", decimal=",", encoding="UTF-16"
        )
        data["target"] = data[6].str[0] + data[7].str[0]
        data.drop(columns=[6, 7], inplace=True)
        categorical_features = list(range(1, 6))
        return data, categorical_features

    def fetch_annealing(self):
        """Download and transform the Annealing Data Set.

        https://archive.ics.uci.edu/ml/datasets/Annealing
        """
        data = pd.read_csv(FETCH_URLS["annealing"], header=None, na_values="?")

        # some features are dropped; they have too many missing values
        missing_feats = (data.isnull().sum(0) / data.shape[0]) < 0.1
        data = data.iloc[:, missing_feats.values]
        data[2].fillna(data[2].mode().squeeze(), inplace=True)

        data = data.T.reset_index(drop=True).T
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)

        categorical_features = [0, 1, 5, 9]
        return data, categorical_features

    def fetch_census(self):
        """Download and transform the Census-Income (KDD) Data Set.

        https://archive.ics.uci.edu/ml/datasets/Census-Income+%28KDD%29
        """
        data = pd.read_csv(FETCH_URLS["census"], header=None)

        categorical_features = (
            list(range(1, 5))
            + list(range(6, 16))
            + list(range(19, 29))
            + list(range(30, 38))
            + [39]
        )

        # some features are dropped; they have too many missing values
        cols_ids = [1, 6, 9, 13, 14, 20, 21, 29, 31, 37]
        categorical_features = np.argwhere(
            np.delete(
                data.rename(columns={k: f"nom_{k}" for k in categorical_features})
                .columns.astype("str")
                .str.startswith("nom_"),
                cols_ids,
            )
        ).squeeze()
        data = data.drop(columns=cols_ids).T.reset_index(drop=True).T
        # some rows are dropped; they have rare missing values
        data = data.iloc[
            data.applymap(lambda x: x != " Not in universe").all(1).values, :
        ]

        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        return data, categorical_features

    def fetch_contraceptive(self):
        """Download and transform the Contraceptive Method Choice Data Set.

        https://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice
        """
        data = pd.read_csv(FETCH_URLS["contraceptive"], header=None)
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [4, 5, 6, 8]
        return data, categorical_features

    def fetch_covertype(self):
        """Download and transform the Covertype Data Set.

        https://archive.ics.uci.edu/ml/datasets/Covertype
        """
        data = pd.read_csv(FETCH_URLS["covertype"], header=None)
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        wilderness_area = pd.Series(
            np.argmax(data.iloc[:, 10:14].values, axis=1), name=10
        )
        soil_type = pd.Series(np.argmax(data.iloc[:, 14:54].values, axis=1), name=11)
        data = (
            data.drop(columns=list(range(10, 54)))
            .join(wilderness_area)
            .join(soil_type)[list(range(0, 12)) + ["target"]]
        )
        categorical_features = [10, 11]
        return data, categorical_features

    def fetch_credit_approval(self):
        """Download and transform the Credit Approval Data Set.

        https://archive.ics.uci.edu/ml/datasets/Credit+Approval
        """
        data = pd.read_csv(
            FETCH_URLS["credit_approval"], header=None, na_values="?"
        ).dropna()
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [0, 3, 4, 5, 6, 8, 9, 11, 12]
        return data, categorical_features

    def fetch_dermatology(self):
        """Download and transform the Dermatology Data Set.

        https://archive.ics.uci.edu/ml/datasets/Dermatology
        """
        data = pd.read_csv(
            FETCH_URLS["dermatology"], header=None, na_values="?"
        ).dropna()
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = list(range(data.shape[1] - 1))
        categorical_features.remove(33)
        return data, categorical_features

    def fetch_echocardiogram(self):
        """Download and transform the Echocardiogram Data Set.

        https://archive.ics.uci.edu/ml/datasets/Echocardiogram
        """
        data = pd.read_csv(
            FETCH_URLS["echocardiogram"],
            header=None,
            error_bad_lines=False,
            warn_bad_lines=False,
            na_values="?",
        )
        data.drop(columns=[10, 11], inplace=True)
        data.dropna(inplace=True)
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [1, 3]
        return data, categorical_features

    def fetch_flags(self):
        """Download and transform the Flags Data Set.

        https://archive.ics.uci.edu/ml/datasets/Flags
        """
        data = pd.read_csv(FETCH_URLS["flags"], header=None)
        target = data[6].rename("target")
        data = data.drop(columns=[0, 6]).T.reset_index(drop=True).T.join(target)
        categorical_features = [
            0,
            1,
            4,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
        ]
        return data, categorical_features

    def fetch_heart_disease(self):
        """Download and transform the Heart Disease Data Set.

        https://archive.ics.uci.edu/ml/datasets/Heart+Disease
        """
        data = (
            pd.concat(
                [
                    pd.read_csv(url, header=None, na_values="?")
                    for url in FETCH_URLS["heart_disease"]
                ],
                ignore_index=True,
            )
            .drop(columns=[10, 11, 12])
            .dropna()
        )
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [1, 2, 5, 6, 8]
        return data, categorical_features

    def fetch_hepatitis(self):
        """Download and transform the Hepatitis Data Set.

        https://archive.ics.uci.edu/ml/datasets/Hepatitis
        """
        data = (
            pd.read_csv(FETCH_URLS["hepatitis"], header=None, na_values="?")
            .drop(columns=[15, 18])
            .dropna()
        )
        target = data[0].rename("target")
        data = data.drop(columns=[0]).T.reset_index(drop=True).T.join(target)
        categorical_features = list(range(1, 13)) + [16]
        return data, categorical_features

    def fetch_german_credit(self):
        """Download and transform the German Credit Data Set.

        https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29
        """
        data = pd.read_csv(FETCH_URLS["german_credit"], header=None, sep=" ")
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = (
            np.argwhere(data.iloc[0, :-1].apply(lambda x: str(x)[0] == "A").values)
            .squeeze()
            .tolist()
        )
        return data, categorical_features

    def fetch_heart(self):
        """Download and transform the Heart Data Set.

        http://archive.ics.uci.edu/ml/datasets/statlog+(heart)
        """
        data = pd.read_csv(FETCH_URLS["heart"], header=None, delim_whitespace=True)
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        categorical_features = [1, 2, 5, 6, 8, 10, 12]
        return data, categorical_features

    def fetch_thyroid(self):
        """Download and transform the Thyroid Disease Data Set.
        Label 0 corresponds to no disease found.
        Label 1 corresponds to one or multiple diseases found.

        https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease
        """
        data = (
            pd.read_csv(FETCH_URLS["thyroid"], header=None, na_values="?")
            .drop(columns=27)
            .dropna()
            .T.reset_index(drop=True)
            .T
        )
        data.rename(columns={data.columns[-1]: "target"}, inplace=True)
        data["target"] = (
            data["target"].apply(lambda x: x.split("[")[0]) != "-"
        ).astype(int)
        categorical_features = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            18,
            20,
            22,
            24,
            26,
            27,
        ]
        return data, categorical_features


class MulticlassDatasets(Datasets):
    """Class to download, transform and save multiclass datasets."""

    def fetch_first_order_theorem(self):
        """Download and transform the First Order Theorem Data Set.

        https://www.openml.org/d/1475
        """
        data = pd.read_csv(FETCH_URLS["first_order_theorem"])
        data.rename(columns={"Class": "target"}, inplace=True)
        return data

    def fetch_gas_drift(self):
        """Download and transform the Gas Drift Data Set.

        https://www.openml.org/d/1476
        """
        data = pd.read_csv(FETCH_URLS["gas_drift"])
        data.rename(columns={"Class": "target"}, inplace=True)
        return data

    def fetch_autouniv_au7(self):
        """Download and transform the AutoUniv au7 Data Set

        https://www.openml.org/d/1552
        """
        data = pd.read_csv(FETCH_URLS["autouniv_au7"])
        data.rename(columns={"Class": "target"}, inplace=True)
        data.target = data.target.apply(lambda x: x.replace("class", "")).astype(int)

        mask = (data.iloc[:, :-1].nunique() > 10).tolist()
        mask.append(True)
        data = data.loc[:, mask].copy()
        return data

    def fetch_autouniv_au4(self):
        """Download and transform the AutoUniv au4 Data Set

        https://www.openml.org/d/1548
        """
        data = pd.read_csv(FETCH_URLS["autouniv_au4"])
        data.rename(columns={"Class": "target"}, inplace=True)
        data.target = data.target.apply(lambda x: x.replace("class", "")).astype(int)

        mask = (data.iloc[:, :-1].nunique() > 10).tolist()
        mask.append(True)
        data = data.loc[:, mask].copy()
        return data

    def fetch_mice_protein(self):
        """Download and transform the Mice Protein Data Set

        https://www.openml.org/d/40966
        """
        data = pd.read_csv(FETCH_URLS["mice_protein"])
        data.rename(columns={"class": "target"}, inplace=True)
        data.drop(columns=["MouseID"], inplace=True)
        data.replace("?", np.nan, inplace=True)

        mask = (data.iloc[:, :-1].nunique() > 10).tolist()
        mask.append(True)
        mask2 = data.isna().sum() < 10
        data = data.loc[:, mask & mask2].dropna().copy()

        data.iloc[:, :-1] = data.iloc[:, :-1].astype(float)

        mapper = {v: k for k, v in enumerate(data.target.unique())}
        data.target = data.target.map(mapper)
        return data

    def fetch_steel_plates(self):
        """Download and transform the Steel Plates Fault Data Set.

        https://www.openml.org/d/40982
        """
        data = pd.read_csv(FETCH_URLS["steel_plates"])

        mask = (data.iloc[:, :-1].nunique() > 10).tolist()
        mask.append(True)
        data = data.loc[:, mask].copy()

        mapper = {v: k for k, v in enumerate(data.target.unique())}
        data.target = data.target.map(mapper)
        return data

    def fetch_cardiotocography(self):
        """Download and transform the Cardiotocography Data Set.

        https://www.openml.org/d/1560
        """
        data = pd.read_csv(FETCH_URLS["cardiotocography"])
        data.rename(columns={"Class": "target"}, inplace=True)

        mask = (data.iloc[:, :-1].nunique() > 10).tolist()
        mask.append(True)
        data = data.loc[:, mask].copy()

        return data

    def fetch_waveform(self):
        """Download and transform the Waveform Database Generator (version 2) Data Set.

        https://www.openml.org/d/60
        """
        data = pd.read_csv(FETCH_URLS["waveform"])
        data.rename(columns={"class": "target"}, inplace=True)
        return data

    def fetch_volkert(self):
        """Download and transform the Volkert Data Set.

        https://www.openml.org/d/41166
        """
        data = pd.read_csv(FETCH_URLS["volkert"])
        data.rename(columns={"class": "target"}, inplace=True)

        mask = (data.iloc[:, 1:].nunique() > 100).tolist()
        mask.insert(0, True)
        data = data.loc[:, mask].copy()
        return data

    def fetch_vehicle(self):
        """Download and transform the Vehicle Silhouettes Data Set.

        https://archive.ics.uci.edu/ml/datasets/Statlog+(Vehicle+Silhouettes)
        """
        data = pd.DataFrame()
        for letter in ascii_lowercase[0:9]:
            partial_data = pd.read_csv(
                urljoin(FETCH_URLS["vehicle"], "xa%s.dat" % letter),
                header=None,
                delim_whitespace=True,
            )
            partial_data = partial_data.rename(columns={18: "target"})
            data = data.append(partial_data)

        mapper = {v: k for k, v in enumerate(data.target.unique())}
        data.target = data.target.map(mapper)

        return data

    def fetch_asp_potassco(self):
        """Download and transform the ASP-POTASSCO Data Set.

        https://www.openml.org/d/41705
        """
        data = pd.read_csv(FETCH_URLS["asp_potassco"], na_values="?")
        data.dropna(inplace=True)
        data["target"] = data["algorithm"]
        data.drop(columns=["instance_id", "algorithm"], inplace=True)

        mask = (data.iloc[:, :-1].nunique() > 100).tolist()
        mask.append(True)
        data = data.loc[:, mask].copy()

        mapper = {v: k for k, v in enumerate(data.target.unique())}
        data.target = data.target.map(mapper)

        return data

    def fetch_wine_quality(self):
        """Download and transform the Wine Quality Data Set.

        https://www.openml.org/d/40691
        """
        data = pd.read_csv(FETCH_URLS["wine_quality"])
        data.rename(columns={"class": "target"}, inplace=True)
        return data

    def fetch_mfeat_zernike(self):
        """Download and transform the Multiple Features Dataset: Zernike Data Set.

        https://www.openml.org/d/22
        """
        data = pd.read_csv(FETCH_URLS["mfeat_zernike"])
        data.drop_duplicates(inplace=True)
        data.rename(columns={"class": "target"}, inplace=True)
        return data

    def fetch_gesture_segmentation(self):
        """Download and transform the Gesture Phase Segmentation Data Set.

        https://www.openml.org/d/4538
        """
        data = pd.read_csv(FETCH_URLS["gesture_segmentation"])
        data.rename(columns={"Phase": "target"}, inplace=True)

        mapper = {v: k for k, v in enumerate(data.target.unique())}
        data.target = data.target.map(mapper)
        return data

    def fetch_texture(self):
        """Download and transform the Texture Data Set.

        https://www.openml.org/d/40499
        """
        data = pd.read_csv(FETCH_URLS["texture"])
        data.drop_duplicates(inplace=True)
        data.rename(columns={"Class": "target"}, inplace=True)
        return data

    def fetch_usps(self):
        """Download and transform the USPS Data Set.

        https://www.openml.org/data/get_csv/19329737/usps.arff
        """
        data = pd.read_csv(FETCH_URLS["usps"])
        data.rename(columns={"int0": "target"}, inplace=True)
        return data

    def fetch_japanese_vowels(self):
        """Download and transform the Japanese Vowels Data Set.

        https://www.openml.org/d/375
        """
        data = pd.read_csv(FETCH_URLS["japanese_vowels"])
        data.rename(columns={"speaker": "target"}, inplace=True)
        data.drop(columns=["utterance", "frame"], inplace=True)
        return data

    def fetch_pendigits(self):
        """Download and transform the Pen-Based Recognition of Handwritten
        Digits Data Set.

        https://www.openml.org/d/32
        """
        data = pd.read_csv(FETCH_URLS["pendigits"])
        data.rename(columns={"class": "target"}, inplace=True)
        return data

    def fetch_image_segmentation(self):
        """Download and transform the Image Segmentation Data Set.

        https://www.openml.org/d/40984
        """
        data = pd.read_csv(FETCH_URLS["image_segmentation"])
        data.drop(columns=data.columns[:5], inplace=True)
        data.rename(columns={"class": "target"}, inplace=True)

        mapper = {v: k for k, v in enumerate(data.target.unique())}
        data.target = data.target.map(mapper)
        return data

    def fetch_baseball(self):
        """Download and transform the Baseball Hall of Fame Data Set.

        https://www.openml.org/d/185
        """
        data = pd.read_csv(FETCH_URLS["baseball"], na_values="?")
        data.drop(columns=["Player", "Position"], inplace=True)
        data.rename(columns={"Hall_of_Fame": "target"}, inplace=True)
        data.dropna(inplace=True)
        return data


class RemoteSensingDatasets(Datasets):
    """Class to download, transform and save remote sensing datasets."""

    def __init__(self, names="all", return_coords=False):
        self.names = names
        self.return_coords = return_coords

    def _load_gic_dataset(self, dataset_name):
        for url in FETCH_URLS[dataset_name]:
            r = requests.get(url, stream=True)
            content = loadmat(io.BytesIO(r.content))
            arr = np.array(list(content.values())[-1])
            arr = np.expand_dims(arr, -1) if arr.ndim == 2 else arr
            if self.return_coords and arr.shape[-1] != 1:
                indices = np.moveaxis(np.indices(arr.shape[:-1]), 0, -1)
                arr = np.insert(arr, [0, 0], indices, -1)
            yield arr

    def fetch_indian_pines(self):
        """Download and transform the Indian Pines Data Set. Label "0" means
        the pixel is not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Indian_Pines
        """
        df = img_array_to_pandas(*self._load_gic_dataset("indian_pines"))
        return df[df.target != 0]

    def fetch_salinas(self):
        """Download and transform the Salinas Data Set. Label "0" means the pixel is
        not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Salinas_scene
        """
        df = img_array_to_pandas(*self._load_gic_dataset("salinas"))
        return df[df.target != 0]

    def fetch_salinas_a(self):
        """Download and transform the Salinas-A Data Set. Label "0" means the pixel is
        not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Salinas-A_scene
        """
        df = img_array_to_pandas(*self._load_gic_dataset("salinas_a"))
        return df[df.target != 0]

    def fetch_pavia_centre(self):
        """Download and transform the Pavia Centre Data Set. Label "0" means the pixel
        is not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Pavia_Centre_scene
        """
        df = img_array_to_pandas(*self._load_gic_dataset("pavia_centre"))
        return df[df.target != 0]

    def fetch_pavia_university(self):
        """Download and transform the Pavia University Data Set. Label "0"
        means the pixel is not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Pavia_University_scene
        """
        df = img_array_to_pandas(*self._load_gic_dataset("pavia_university"))
        return df[df.target != 0]

    def fetch_kennedy_space_center(self):
        """Download and transform the Kennedy Space Center Data Set. Label "0"
        means the pixel is not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Kennedy_Space_Center_.28KSC.29
        """
        df = img_array_to_pandas(*self._load_gic_dataset("kennedy_space_center"))
        return df[df.target != 0]

    def fetch_botswana(self):
        """Download and transform the Botswana Data Set. Label "0" means the pixel is
        not labelled. It is therefore dropped.

        http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes#Botswana
        """
        df = img_array_to_pandas(*self._load_gic_dataset("botswana"))
        return df[df.target != 0]
