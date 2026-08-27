#include <stack>
using namespace std;
class MinStack {
private:
    stack<int> s;
    stack<int> m;
public:
    MinStack() { }
    
    void push(int val) {
        if (m.empty() || val <= m.top())
            m.push(val);
        s.push(val);
    }
    
    void pop() {
        int p = s.top();
        s.pop();
        if (p == m.top())
            m.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return m.top();
    }
};
