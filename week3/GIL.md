# GIL(Global Interpreter Lock)
GIL을 알고 있지만 자꾸 헷갈려서 한번 정리를 해볼까 한다.

## GIL이란 무엇인가.
In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.

python wiki의 말이다.

CPython에서의 GIL은 Python 코드(bytecode)를 실행할 때에 여러 thread를 사용할 경우, 단 하나의 thread만이 Python object에 접근할 수 있도록 제한하는 mutex 이다. 그리고 이 lock이 필요한 이유는 CPython이 메모리를 관리하는 방법이 thread-safe하지 않기 때문이다.

[출처 : 개발새발블로그](https://dgkim5360.tistory.com/entry/understanding-the-global-interpreter-lock-of-cpython)

나는 mutex도 모른다. 그래서 이번에 정리했다.  
[mutex & semaphore 참고](./mutex_semaphore.md) 

## CPython의 메모리 관리 : Reference Counting
- CPython은 Reference Counting이라는 개념이 있다.
- 이는 메모리 관리방법인데, object마다 몇 개의 reference가 
있는지를 항상 count하고 있다는 말이다. 아래에 예시가 있다.
- 이는 GIL을 선택하게 되는 이유가 되었다.
  - 살아있어야하는 object를 죽이는 등의 참사가 일어날 수 있다.

```py
import sys
a = []
b = a
sys.getrefcount(a)
# 3
```
## 귀도 반 로섬의 말
I’d welcome a set of patches into Py3k only if the performance for a single-threaded program (and for a multi-threaded but I/O-bound program) does not decrease.

단일 thread 프로그램에서의 성능을 저하시키지 않고 GIL의 문제점을 개선할 수 있다면, 나는 그 개선안을 기꺼이 받아들일 것이다.

그리고 지금까지 받아들여진 개선안은 없다.

\
\
\
다음에는 GC(garbage Collection)기법을 알아보자.