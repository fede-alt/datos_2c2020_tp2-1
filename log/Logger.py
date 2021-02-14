
class Logger:

    __logfile_name = "tabulations.txt"
    __header = ["ID","Model", "Hyperparameters", "Features", "Score", "Nota"]

    @classmethod
    def log_model(cls, model, hyperparameters, features, score, notes="" ,verbose=True):

        line = model+","
        line += "#".join([name+":"+str(value) for name,value in hyperparameters.items()])+","
        line += "#".join(features)+","
        line += str(round(score, 4))+"\n"

        if verbose:
            print("Writing..")
            print(f"Model => {model}")
            print(f"Hyperparameters => {len(hyperparameters)}")
            for param, value in hyperparameters.items():
                print(f"\t{param}: {value}")
            print(f"Features =>  {len(features)}")
            for feature in features:
                print(f"\t{feature}")
            print(f"Score => {score}")

        with open(Logger.__logfile_name, "r+") as file:

            idx = 0
            while file.readline(): idx += 1

            line = str(idx) + ","+ line
            file.write(line)

        print("Model logged successfully")

    @classmethod
    def get_header(cls, listed=True):

        if listed:
            return Logger.__header
        return ",".join(Logger.__header)
