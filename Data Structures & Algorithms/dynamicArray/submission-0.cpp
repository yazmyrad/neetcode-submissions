class DynamicArray {
public:
    int *arr;
    int length = 0;
    int cap = 0;
    DynamicArray(int capacity) {
        try{
            arr = new(std::nothrow) int[capacity];
            cap = capacity;
        }
        catch(...){
            cout<<"Error in constructor"<<endl;
        }
    }

    int get(int i) {
        return *(arr + i);
    }

    void set(int i, int n) {
        try{
            *(arr+i) = n;
        }catch(...){
            cout<<"Error in set"<<endl;
        }
    }

    void pushback(int n) {
        try{
            if(length == cap){
                resize();
            }
            *(arr+length) = n;
            length += 1;
        }catch(...){
            cout<<"Error in push"<<endl;
        }
    }

    int popback() {
        try{
            int val = *(arr+length-1);
            length -= 1;
            return val;
        }catch(...){
            cout<<"Error"<<endl;
        }
        return 888;
    }

    void resize() {
        try{
            int *newarr = new(std::nothrow) int[2*cap];
            if (newarr == nullptr){
                return;
            }
            cap = 2*cap;
            for (int i = 0; i < length; i++){
                *(newarr + i) = *(arr + i);
            }
            delete[] arr;
            arr = newarr;
        }catch(...){
            cout<<"Error in resize"<<endl;
        }
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return cap;
    }

    ~DynamicArray(){
        delete[] arr;
    }
};
