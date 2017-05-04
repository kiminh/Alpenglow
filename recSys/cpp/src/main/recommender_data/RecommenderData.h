
#ifndef RECOMMENDER_DATA
#define RECOMMENDER_DATA
/* RecommenderData class
   
   RecommenderData reads scrobble files and stores RecDats.
*/

#include <math.h>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include "../utils/SpMatrix.h"
#include "AttributeContainer.h"

using namespace std;

struct Location {
  int location_id;
  double x;
  double y;
  double z;
};


struct Tweet {
  double time;
  double x;
  double y;
  double z;
  int location_id;
  double distance;
};


struct RecDat{
  int id;
  double score;
  double time;
  int user,item,eval;
  int category;
  Location location;
  // std::vector<std::vector<int>> *attributes;
  //bool operator<(const RecDat& rec_dat) const { return score < rec_dat.score; }
  //bool operator>(const RecDat& rec_dat) const { return score > rec_dat.score; }
  friend ostream &operator<<( ostream &output, const RecDat &rec_dat ){ 
     output << "t=" << (int) rec_dat.time << " u=" << rec_dat.user << " i=" << rec_dat.item << " s=" << rec_dat.score;
     return output;            
  }
};
typedef vector <RecDat> RecDats;

typedef map <int,double> Recommendation;
typedef map <int,double> :: iterator RecIterator;

struct RecPred{
  double score;
  double prediction;
};
typedef vector <RecPred> Predictions;
typedef vector <double> Gradients;

struct RecommenderDataParameters{
  string file_name;
  string type;
};
class RecommenderData{
  public:
    RecommenderData(){recMatrix.clear();maxTime=0;};
    RecommenderData(RecommenderDataParameters* params){
      fileName = params->file_name;
      type = params->type;
    }
    ~RecommenderData(){};
    void readFromFile(string file_name, string type){ read_from_file(file_name, type); }
    void read_from_file(string file_name, string type);
    void read_from_file_core(istream& ifs, string type);
    void setRecDats(RecDats recData){ this->recData = recData; }
    RecDat* get(int idx){return &(recData[idx]);}
    int size(){return recData.size();}
    SpMatrix* matrix();
    vector<int>* items();
    vector<int>* users();
    void setMaxTime(double _maxTime){ maxTime = _maxTime; }
    RecDats* getRecData(){ return &recData; }
    void init(){
      readFromFile(fileName, type);
    }
    void set_attribute_container(InlineAttributeReader* attribute_container){
      attribute_container_ = attribute_container;
    }
  private:
    RecDats recData;
    SpMatrix recMatrix;
    vector<int> items_;
    vector<int> users_;
    double maxTime;
    string fileName;
    string type;
    InlineAttributeReader* attribute_container_;
};

#endif