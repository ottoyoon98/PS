#include <iostream>

using namespace std;

int main()
{
    int T;
    int P, Q, A, B, C, D;
    int bit, berry, coin, bitcoin;
    int times;

    cin >> T;

    for(int i = 0 ; i < T ; i++){
        cin >> P >> Q >> A >> B >> C >> D;
        bit = P;
        berry = Q;
        coin = bitcoin = 0;

        // berry to coin
        times = berry/C;
        berry -= times*C;
        coin += times*D;

        // bit to coin
        times = bit/A;
        bit -= times*A;
        coin += times*B;

        times = (coin-bit)/(A+B);
        bitcoin = max(min(bit+A*times, coin-B*times), min(bit+A*(times+1), coin-B*(times+1)));

        cout << bitcoin << "\n";
    }
    return 0;
}
