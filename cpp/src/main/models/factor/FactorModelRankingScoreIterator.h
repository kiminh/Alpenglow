#ifndef FACTOR_MODEL_RANKING_SCORE_ITERATOR_H
#define FACTOR_MODEL_RANKING_SCORE_ITERATOR_H

#include "../RankingScoreIterator.h"
#include "lemp/LempContainer.h"
#include <utility>

using namespace std;

class FactorModelRankingScoreIterator : public RankingScoreIterator{
public:
  FactorModelRankingScoreIterator(vector<double> user_factor, LempContainer *container)
  : user_factor_(user_factor),
    container_(container)
  {
    next_bucket_ = container_->buckets_begin();
    user_factor_norm_ = Util::norm(&user_factor);
  }

  FactorModelRankingScoreIterator(){};

  bool has_next(double upper_bound) override;
  using RankingScoreIterator::has_next;
  pair<int, double> get_next() override;
  int unique_items_num() override;
protected:
  double user_factor_norm_;
  vector<double> user_factor_;
  LempContainer *container_ = NULL;
  multiset<LempBucket*>::iterator next_bucket_;
  vector<pair<int,double>> current_scores_;
};

#endif /* FACTOR_MODEL_RANKING_SCORE_ITERATOR_H */
