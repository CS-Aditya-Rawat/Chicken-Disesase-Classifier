
from chicken_disease_classifier.config.configuration import ConfigurationManager
from chicken_disease_classifier.components.evaluation import Evaluation
from chicken_disease_classifier import logger


STAGE_NAME="Evaluation"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == "__main__":
    try:
        logger.info(f"*********************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==============x")
    except Exception as e:
        logger.exception(e)
        raise e