#include <bits/stdc++.h>

using namespace std;

int a[41][41];

int main()
{
    for(int i=0; i<13 ; i++)            //Blue line from central to airport
    {
        a[i][i+1]=1;
        a[i+1][i]=1;
    }
    a[0][14]=1;                         //Red line from central to egmore
    a[14][0]=1;
    for(int i=14; i<26 ; i++)           //Red line from egmore to tambaram
    {
        a[i][i+1]=1;
        a[i+1][i]=1;
    }
    a[19][20]=0;                        //removing saidapet and st.thomas mount egde
    a[20][19]=0;
    a[19][9]=1;                         //saidapet to guindy
    a[9][19]=1;
    a[9][20]=1;                         //guindy to st.thomas mount
    a[20][9]=1;
    a[22][23]=0;                        //remove meenambakam to pallavaram
    a[23][22]=0;
    a[22][13]=1;                        //meenambakam to airport (tirusulam)
    a[13][22]=1;
    a[13][23]=1;                        //airport to pallavaram
    a[23][13]=1;
    
    a[14][27]=1;                        //green line egmore to nehru park metro
    a[27][14]=1;
    for(int i=27; i<39 ; i++)           //green line nehru park to ekatuthangal
    {
        a[i][i+1]=1;
        a[i+1][i]=1;
    }
    a[39][10]=1;                        //ekatuthangal to alandur
    a[10][39]=1;
    a[10][20]=1;                        //alandur to St.Thomas mount
    a[20][10]=1;
    for(int i=0; i<40 ; i++)            //Prints full matrix
    {
        for (int j=0; j<40 ; j++)
        {
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

