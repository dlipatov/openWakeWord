import yaml

config = yaml.load(open("./examples/custom_model.yml", 'r').read(), yaml.Loader)

# Modify values in the config and save a new version
config["cpu_max_load"] = 0.85
config["preferred_device"] = "cpu"
config["custom_negative_phrases"] = [
    "Нифиня",
    "Афоня",
    "Ниуфуня",
    "Нюфоня",
    "Афоня",
    "На Фене",
    "Эй Феня!",
    "на фанере", 
    "Фефеня"
]
config["target_phrase"] = ["Нафаня!"]
config["model_name"] = "nafanya"
config["n_samples"] = 1000
config["n_samples_val"] = 1000
config["steps"] = 10000
config["target_accuracy"] = 0.6
config["target_recall"] = 0.25
config["rir_paths"] = ["./mit_rirs"]
config["piper_sample_generator_path"] = "./piper-sample-generator"
config["piper_model_path"] = './piper-model/ru/medium/irina.pt'
config["piper_max_speakers"] = 1
config["batch_n_per_class"] = {
    "adversarial_negative": 50,
    "positive": 50
}
config["false_positive_validation_clips"] = "./false_positive_clips"
config["feature_data_clips"] = {
    "cv11":"./cv11_ru_16k/ru_test_0",
    "cv16": "./cv_16_ru/wav_16k"
}
config["skip_generated_adversarial_texts"] = True
config["background_paths"] = ['./audioset_16k', './fma']
config["custom_positive_train"] = "./custom_positive_train"
config["custom_positive_test"] = "./custom_positive_test"

# these settings will be updated during features generation
config["false_positive_validation_data_path"] = ""
config["feature_data_files"] = {}

with open('./nafanya.yaml', 'w') as file:
    documents = yaml.dump(config, file)