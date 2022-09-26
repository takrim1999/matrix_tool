#include<iostream>
using namespace std;
int determinant( int n;int p[n][n]){
   
   int m1=0;
   for(int i=0; i<n;i++)
    { 
        m1=p[i][i]*p[i+1][i+1] - p[i][i+1]p[i+1][i];

        
    }
   
}
int main()
{
    int n ;
    cout<<"Enter the order of the matrix :";
    cin>>n;
    int A[n][n];
    
    for(int i=0; i<n;i++)
    { cout <<"Enter row on."<< i+1 <<":";
        for(int j=0; j<n;j++)
    {
        cin>>A[i][j];
    }
        
    } cout<<"Matrix A is :"<<endl;
    for(int i=0; i<n;i++)
    { 
        for(int j=0; j<n;j++)
    {
        cout<<A[i][j]<<"  ";
    }
    cout<<endl;
     cout<<"\t  "<<"   " ;  
    }
    cout<<endl;
    int B[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0; j<n;j++)
    {
        B[i][j]=A[j][i];
    }
    }
    cout<<"The transpose matrix of A is :"<<endl;
    for(int i=0;i<n;i++)
    {
        for(int j=0; j<n;j++)
    {
        cout<< B[i][j] <<"  ";
    }
    cout<<"\n";
    }
    int trace=0;
    for(int i=0;i<=n;i++)
    {
        for(int j=0; j<n;j++)
    {
        if(i==j){
            trace +=A[i][j];
        }
    }
    }
    cout<<"Trace is = "<<trace<<endl;

    return 0;
}