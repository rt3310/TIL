# 투 포인터
- 투 포인터(Two Pointer)에는 여러 가지 방식이 있지만, 대개는 시작점과 끝점 또는 왼쪽 포인터와 오른쪽 포인터 두 지점을 기준으로 하는 문제 풀이 전략을 뜻한다.
- 범위를 좁혀 나가기 위해서는, 일반적으로 배열이 정렬되어 있을 때 좀 더 유용하다.

|1|2|3|4|5|
|-|-|-|-|-|
|^||||^|

|1|2|3|4|5|
|-|-|-|-|-|
||^|||^|

|1|2|3|4|5|
|-|-|-|-|-|
|||^|^||

- 투 포인터는 위와 같이 주로 정렬된 배열을 대상으로 하며, 2개의 포인터가 좌우로 자유롭게 움직이며 풀이한다.