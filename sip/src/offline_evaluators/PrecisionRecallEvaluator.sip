
struct PrecisionRecallEvaluatorParameters {
  %TypeHeaderCode
  #include "offline_evaluators/PrecisionRecallEvaluator.h"
  %End
  %Docstring
  Constructor parameter struct for :py:class:`alpenglow.cpp.PrecisionRecallEvaluator`. See documentation there.
  %End
  int cutoff;
  std::string test_file_name;
  std::string test_file_type;
  int time;
};

class PrecisionRecallEvaluator : public OfflineEvaluator{
  %TypeHeaderCode
  #include "offline_evaluators/PrecisionRecallEvaluator.h"
  %End
  public:
    PrecisionRecallEvaluator(PrecisionRecallEvaluatorParameters* params);
    void set_model(Model* model);
    void set_train_data(RecommenderData* recommender_data);
    void evaluate();
    bool self_test();
};

