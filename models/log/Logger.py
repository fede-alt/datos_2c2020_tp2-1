from datetime import datetime


class Logger:
    __logfile_name = "log/tabulations.txt"
    __header = ["ID", "Model Name", "Score", "Kaggle Score", "Notes" ,"Hyperparameters", "Features"]

    @classmethod
    def log_model(cls, model_name, score, kaggle_score=-1, notes="", dataset_name="", hyperparams={}, verbose=False):

        now = datetime.now()
        line = str(datetime.timestamp(now)) + ","
        line += model_name + ","
        line += str(round(score, 6)) + ","
        line += str(round(kaggle_score,6)) + ","
        line += notes + ","
        line += dataset_name + ","
        line += "#".join([name + ":" + str(value) for name, value in hyperparams.items()]) + "\n"

        if verbose:
            print("Writing..")
            print(f"Model name => {model_name}")
            print(f"Score => {score}")
            print(f"Kaggle score => {kaggle_score if kaggle_score > 0 else '--'}")
            print(f"Dataset name => {dataset_name}")
            print(f"Hyperparameters => {len(hyperparams)}")
            for param, value in hyperparams.items():
                print(f"\t{param}: {value}")


        with open(Logger.__logfile_name, "r+") as file:
            file.read()
            file.write(line)

        print("Model logged successfully")

    @classmethod
    def get_header(cls, listed=True):

        if listed:
            return Logger.__header
        return ",".join(Logger.__header)
