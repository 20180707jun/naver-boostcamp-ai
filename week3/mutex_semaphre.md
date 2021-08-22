# Critical Section & mutex & semaphore
구글에 검색해보니 같이 나오길래 같이 정리해본다.

## Critical Section
- 하나에 한스레드만 진입해야하는 특정 코드 구역

## mutex & semaphore
### Mutex
- MUTual EXclusion, 한글로 상호 배제
- 1개의 락만 갖는 Locking 메커니즘
- critical Section은 가진 Thread들이 running time이 서로 겹치지 않게, 각각 단독으로 실행되게 하는 기술.

### semaphore
- 역시 dead lock을 피하기 위한 기술 중에 하나
- Signaling 메커니즘이라는 점에서 뮤텍스와 다르다.
- 세마포어는 락을 걸지 않은 쓰레드도 Signal을 보내 락을 해제할 수 있다.
- Counting Semaphore와, Binary Semaphore가 있다.
  - Counting Semaphore : n개의 스레드를 허용, 그 이상은 락이 실행
  - Binary Semaphoreㅇ: 1개의 스레드를 허용, Mutex와 흡사하다.

### 둘의 공통점
- Critical section에 접근하는 기술
- 서로 튜링동치이다.
  - 튜링 도치란? : 컴퓨터 P, Q가 있을 때, P가 할 수 있는 일들을 Q가 모두 흉내낼 수 있고, Q가 할 수 있는 일들을 P가 모두 흉내낼 수 있다면 두 컴퓨터는 튜링 동치이다.

### 둘의 차이점
- semaphore는 여러개의 스레드(또는 프로세스)가 접근이 가능하다. - 뮤텍스는 1개의 스레드(또는 프로세스)만 접근이 가능하다.
- semaphore는 여러개의 스레드가 접근가능하기에, 다른 프로세스가 semaphore를 해제할 수 있다.
- 뮤텍스는 락을 획득한 프로세스가 반드시 그 락을 해제해야한다.

