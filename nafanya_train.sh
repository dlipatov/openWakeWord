python3 ./create_config.py
python3 ./openwakeword/train.py --training_config ./nafanya.yaml --generate_clips
python3 ./openwakeword/train.py --training_config ./nafanya.yaml --augment_clips
python3 ./openwakeword/train.py --training_config ./nafanya.yaml --compute_features
python3 ./openwakeword/train.py --training_config ./nafanya.yaml --compute_false_positive
python3 ./openwakeword/train.py --training_config ./nafanya.yaml --train_model
