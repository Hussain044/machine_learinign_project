from housing.constant import DATA_VALIDATION_CONFIG_KEY
from housing.pipeline.pipeline import Pipeline
import logging
from housing.config.configuration import Configuration


def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
        # model_trainer_config = Configuration().get_model_trainer_config()
        # print(model_trainer_config)
    except Exception as e:
        logging.error(f"e")
        print(e)


if __name__ == '__main__':
    main()
