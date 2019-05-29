#include "ExperimentEnvironment.h"
#include "OnlineExperiment.h"


void ExperimentEnvironment::set_parameters(OnlineExperimentParameters* params){
  top_k_ = params->top_k;
  evaluation_start_time_ = params->evaluation_start_time;
  experiment_termination_time_ = params->experiment_termination_time;
  exclude_known_ = params->exclude_known;
  initialize_all_ = params->initialize_all;
  max_user_ = params->max_user;
  max_item_ = params->max_item;
  if (initialize_all_ && max_user_>0){
    for(int i=0;i<=max_user_;i++) users_.push_back(i);
  }
  if (initialize_all_ && max_item_>0){
    for(int i=0;i<=max_item_;i++) items_.push_back(i);
  }
}
void ExperimentEnvironment::update(RecDat* rec_dat){
  int item = rec_dat->item;
  int user = rec_dat->user;
  double score = rec_dat->score; 

  if (!GET_VECTORMAP(item_map_,item,false)){
    new_item_=true;
    PUT_VECTORMAP(item_map_,item,true);
    if (!initialize_all_) items_.push_back(item);
  } else {
    new_item_=false;
  }
  if (!GET_VECTORMAP(user_map_,user,false)){
    first_occurrence_of_user_=true;
    PUT_VECTORMAP(user_map_,user,true);
    users_.push_back(user);
  } else {
    new_user_=false;
  }
  if(train_matrix_.get(user,item)==0){
    item_new_for_user_=true;
    train_matrix_.update(user,item,score);
  } else {
    item_new_for_user_=false;
  }
  popularity_sorted_container_.increase(item);
  popularity_container_.increase(item);
}
