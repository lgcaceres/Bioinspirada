#include <iostream>
#include <fstream>

#include <math.h>
#include <cmath> 
#include <stdlib.h>
//#include <stdio.h>
#include <cstring>


#include <iomanip>      // std::setprecision

#include <fstream>      // std::ofstream


#include<vector>
#define earthRadiusKm 6371.0


using namespace std;


#define LENBUFF 50
#define SETPRECISIONDOUBLE 3
#define LENVEC 21
#define FILEIN "miraflores.txt"
#define FILEOUT "distances-miraflores.txt"



typedef vector< pair<double,double> > vecCoor;
typedef vector< pair<double,double> >::iterator itvecCoor;
typedef vector< vector<double> > matrix;



// This function converts decimal degrees to radians
double deg2rad(double deg) {
  return (deg * M_PI / 180);
}

//  This function converts radians to decimal degrees
double rad2deg(double rad) {
  return (rad * 180 / M_PI);
}

/**
 * Returns the distance between two points on the Earth.
 * Direct translation from http://en.wikipedia.org/wiki/Haversine_formula
 * @param lat1d Latitude of the first point in degrees
 * @param lon1d Longitude of the first point in degrees
 * @param lat2d Latitude of the second point in degrees
 * @param lon2d Longitude of the second point in degrees
 * @return The distance between the two points in KILOMETERS
 */
double distanceEarth(double lat1d, double lon1d, double lat2d, double lon2d) {
  double lat1r, lon1r, lat2r, lon2r, u, v;
  lat1r = deg2rad(lat1d);
  lon1r = deg2rad(lon1d);
  lat2r = deg2rad(lat2d);
  lon2r = deg2rad(lon2d);
  u = sin((lat2r - lat1r)/2);
  v = sin((lon2r - lon1r)/2);
  return 2.0 * earthRadiusKm * asin(sqrt(u * u + cos(lat1r) * cos(lat2r) * v * v));
  //return 2.0 * earthRadiusKm * asin(sqrt(u * u + cos(lat1r) * cos(lat2r) * v * v))*1000;
}



void  matrix_distances(matrix& mymat, vecCoor& myvec,int lenVec)
{


  itvecCoor it1 = myvec.begin();

  for(int i=0 ; i<lenVec ; i++){
    itvecCoor it2 = myvec.begin();
    for(int j=0 ; j<lenVec ; j++){
      double temp = 0.0;
      temp = distanceEarth(it1->first,it1->second,it2->first,it2->second);      
      mymat[i][j]=temp;
      it2++;
    }
    it1++;
  }
}

void create_mat(matrix& mymat, int num_row, int num_col)
{
  mymat.resize(num_row);
  for ( int i = 0 ; i < num_row ; i++ )
  {
      mymat[i].resize(num_col);
  }

}

void load_file(vecCoor& myvec)
{


  char buff[LENBUFF];
  char* pt = NULL;

  ifstream file;
  file.open(FILEIN,ifstream::in);
  
  while(!file.eof())
  { 
    char lat[LENBUFF];
    char lon[LENBUFF];
    file.getline(buff,LENBUFF);
    pt = strtok(buff," ");
    sprintf(lat,"%s",pt);
    pt = strtok(NULL," ");
    sprintf(lon,"%s",pt);
    myvec.push_back(make_pair(atof(lat), atof(lon)));
  }
  file.close();
}


void print_matrix(matrix& mymat, int lenVec)
{
  for(int i=0 ; i<lenVec ; i++){
    for(int j=0 ; j<lenVec ; j++){
      cout<<fixed;
      cout<<setprecision(SETPRECISIONDOUBLE)<<mymat[i][j];
      cout<<" ";
    }
    cout<<endl;
  }
}



void print_file(matrix& mymat, int lenVec){
  ofstream ofs (FILEOUT, std::ofstream::out);
  for(int i=0 ; i<lenVec ; i++){
    for(int j=0 ; j<lenVec ; j++){
      ofs<<fixed;
      ofs<<setprecision(SETPRECISIONDOUBLE)<<mymat[i][j];
      ofs<<" ";
    }
    ofs<<endl;
  }
  ofs.close();
}

int main(){


  
  vecCoor myvec;
  load_file(myvec);

  matrix mymat;
  create_mat(mymat,LENVEC,LENVEC);
  matrix_distances(mymat,myvec,LENVEC);

  print_matrix(mymat,LENVEC);
  print_file(mymat,LENVEC);



	return 0;
}