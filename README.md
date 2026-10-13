# textstats

텍스트 통계를 내는 작은 Python 함수 모음입니다.

## 사용법

### word_count

공백으로 구분된 단어의 수를 셉니다.

```python
from textstats import word_count

word_count("hello world")        # 2
word_count("hello - !! world!")  # 2
word_count("안녕 … 세상")         # 2  ("…"는 유니코드 구두점)
word_count("「 」 안녕 。")        # 1  ("「", "」", "。"는 유니코드 구두점)
word_count("가격 € 5")           # 3  ("€"는 기호(Sc)라서 단어로 셈)
```

- 구두점만으로 된 토큰(예: `"-"`, `"!!"`)은 세지 않습니다.
- 단어에 붙은 구두점(`world!`)은 한 단어로 셉니다.
- 구두점의 기준은 ASCII 구두점(`string.punctuation`)과 유니코드 범주 `P*`(`…`, `—`, `「`, `。` 등)입니다.
- 유니코드 기호 범주 `S*`(`€`, `→` 등)는 구두점이 아니므로 이런 문자로만 된 토큰도 단어로 셉니다.
  (단, `+`, `=`처럼 `string.punctuation`에 속한 ASCII 문자는 구두점으로 봅니다.)

### char_frequency

각 문자가 나타난 횟수를 딕셔너리로 돌려줍니다.

```python
from textstats import char_frequency

char_frequency("aab b")  # {'a': 2, 'b': 2}
char_frequency("aA!!")   # {'a': 1, 'A': 1, '!': 2}
```

- 공백은 세지 않습니다.
- 유니코드 공백(NBSP `U+00A0`, 전각 공백 `U+3000` 등)도 세지 않습니다.
- 대소문자를 구분합니다.
- 구두점은 다른 문자처럼 셉니다.

## 테스트

```
python -m unittest
```
