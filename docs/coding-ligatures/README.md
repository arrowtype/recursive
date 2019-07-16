# coding-ligatures-README

Special ligatures dedicated for coders. The ligatures are based on the most common character combinations used in languages like Python or JavaScript.

## Glyph naming standard

Naming glyphs follows simple formula:

The main part of ligature's name is build with source glyphs' names separated by `_`. Every coding ligature has suffix `.code`.

- `sourceGlyphNameA_sourceGlyphNameB_sourceGLyphNameC.code`

- _example:_
  glyph constructed out of `slash` and `asterix` will be named `slash_asterix.code`

#`maybe this should be truth only for the operators? in other situations we would't use underscores?`

## Planning work

Work was divided into 3 stages that corresponds to different priority levels

### _priority 1_

#### logic operators

| ligature     | name                     | usecase        |
| ------------ | ------------------------ | -------------- |
| ==           | equal_equal.code         | Python, JS     |
| !=           | exclam_equal.code        | Python, JS     |
| ===          | equal_equal_equal.code   | Python, JS     |
| >=           | greater_equal.code       | JS, Python, C# |
| <=           | less_equal.code          | JS, Python, C# |
| !==          | exclam_equal_equal.code  | JS             |
| =/=          | equal_slash_equal.code   |
| !!           | exclam_exclam.code       | JS             |
| ??           | question_question.code   | C#             |
| %%           | percent_percent.code     |
| &&           | ampersand_ampersand.code |
| &#124;&#124; | bar_bar.code             | JS             |
| ?.           | question_period.code     |
| ?:           | question_colon.code      |
| ?:           | question_colon.code      |

#### arrows & more

| ligature | name               | usecase            |
| -------- | ------------------ | ------------------ |
| =>       | equal_greater.code | JS arrow functions |

#### math operators

| ligature | name                         | usecase |
| -------- | ---------------------------- | ------- |
| +        | plus.code                    |
| ++       | plus_plus.code               |
| +++      | plus_plus_plus.code          |
| -        | hyphen.code                  |
| --       | hyphen_hyphen.code           |
| ---      | hyphen_hyphen_hyphen.code    |
| \*       | asterix.code                 |
| \*\*     | asterix_asterix.code         | JS      |
| \*\*\*   | asterix_asterix_asterix.code | Haskell |
| +=       | plus_equal.code              | JS, SQL |
| -=       | minus_equal.code             | JS, SQL |
| \*=      | asterisk_equal.code          | JS, SQL |
| /=       | slash_equal.code             | JS, SQL |

#### comments and others

| ligature | name                                     |
| -------- | ---------------------------------------- |
| \_\_     | underscore_underscore.code               |
| /\*      | slash_asterix.code                       |
| \*/      | asterix_slash.code                       |
| //       | slash_slash.code                         |
| ///      | slash_slash_slash.code                   |
| '''      | quotesingle_quotesingle_quotesingle.code |
| """      | quotedbl_quotedbl_quotedbl.code          |
| #        | numbersign.code                          |
| ##       | numbersign_numbersign.code               |
| ###      | numbersign_numbersign_numbersign.code    |

### _prority 2_

#### Haskell-specific ligatures

| ligature     | name                               | usecase          |
| ------------ | ---------------------------------- | ---------------- |
| &&&          | ampersand_ampersand_ampersand.code | Haskell          |
| &#124;&#124; | bar_bar_bar.code                   | Haskell          |
| ->           | hyphen_greater.code                | Haskell          |
| >-           | greater_hyphen.code                | Haskell          |
| <-           | less_hyphen.code                   | Haskell          |
| -<           | hyphen_less.code                   | Haskell          |
| ::           | colon_colon.code                   | Haskell          |
| >>           | greater_greater.code               | Haskell          |
| >>>          | greater_greater_greater.code       | Haskell          |
| <<           | less_less.code                     | Haskell          |
| <<<          | less_less_less.code                | Haskell          |
| <            | less.code                          | (matching sizes) |
| <            | greater.code                       | (matching sizes) |

`# I'm still not sure about making special brackets`

#### string formatting operators and escape characters

| ligature | name |
| -------- | ---- |
| %c       |      |
| %d       |      |
| %s       |      |
| %g       |      |
| %r       |      |
| \n       |      |
| \b       |      |
| \r       |      |
| \t       |      |
| \v       |      |
| \'       |      |
| \"       |      |
| \\       |      |
| %%       |      |

#### bracket combinations

| ligature | name                           |
| -------- | ------------------------------ |
| {[       | braceleft_bracketleft.code     |
| ]}       | bracketright_braceright.code   |
| [[       | bracketleft_bracketleft.code   |
| ]]       | bracketright_bracketright.code |
| [(       | bracketleft_parenleft.code     |
| )]       | parenright_bracketright.code   |
| {(       | braceleft_parenleft.code       |
| )}       | parenright_braceright.code     |
| ((       | parenleft_parenleft.code       |
| ))       | parenright_parenright.code     |

- _priority 3_

#### Powerline symbols

| glyph | name    |
| ----- | ------- |
|      | uniE0A0 |
| ☐     | uni2610 |
| ☑     | uni2611 |

#### extra markdown ligatures (Will `space` glyphs work in clig? Needs testing in code editors!)

We could create the stylistic set that "emulates" mark down behaviour. With ligatures for `[]` , `[x]` etc

| ligature | name                                         | usecase                    |
| -------- | -------------------------------------------- | -------------------------- |
| - [ ]    | hyphen_space_braceleft_space_braceright.code | markdown to-do, incomplete |
| - [x]    | hyphen_space_braceleft_x_braceright.code     | markdown to-do, complete   |

#### keywords

| ligature | name |
| -------- | ---- |
| var      |      |
| const    |      |
| let      |      |
| if       |      |
| else     |      |
| elif     |      |
| switch   |      |
| case     |      |
| for      |      |
| while    |      |
| in       |      |
| not      |      |
| try      |      |
| except   |      |
| catch    |      |
| assert   |      |
| def      |      |
| function |      |
| class    |      |
| self     |      |
| print    |      |
| and      |      |
| or       |      |
| return   |      |
| true     |      |
| True     |      |
| false    |      |
| False    |      |
| do       |      |

#### (more) language specific keywords

| ligature   | name |
| ---------- | ---- |
| import     |      |
| #include   |      |
| void       |      |
| int        |      |
| str        |      |
| char       |      |
| float      |      |
| double     |      |
| long       |      |
| alloc      |      |
| dealloc    |      |
| printf     |      |
| func       |      |
| \*argv     |      |
| \*args     |      |
| \*\*kwargs |      |
| def        |      |
| class      |      |
| self       |      |
| print      |      |
| and        |      |
| or         |      |
| return     |      |
| **init**   |      |
| **del**    |      |
| **iter**   |      |
| **repr**   |      |

## Syntax examples for testing

### Python

```Python
    class Person(object):
    	# my new class
    	isMale = randrange(0,1)

    	def __init__(self, name, height):
    		self.name = name
    		self.height = height
    		self.isTall = True if height > 180
    		self.age = randrange(0,100)

    	def getAge(self) -> int:
    		'''
    			getter for age value
    		'''
    		return self.age

    if __name__ == "__main__":
    	mark = Person("Mark:, 190)
    	if mark.isTall:
    		print("Mark is really tall")
    	else:
    		print("Mark is not that tall")
```

### JavaScript

```JavaScript
    var rows = prompt("How many rows for your multiplication table?");
    var cols = prompt("How many columns for your multiplication table?");
    if(rows == "" || rows == null)
    	rows = 10;
    if(cols== "" || cols== null)
       	cols = 10;
        createTable(rows, cols);
        function createTable(rows, cols)
        {
          var j=1;
          var output = "<table border='1' width='500' cellspacing='0'cellpadding='5'>";
          for(i=1;i<=rows;i++)
          {
        	output = output + "<tr>";
            while(j<=cols)
            {
      		  output = output + "<td>" + i*j + "</td>";
       		  j = j+1;
       		}
       		 output = output + "</tr>";
       		 j = 1;
        }
        output = output + "</table>";
        document.write(output);
    }
```

# Resources

## JavaScript

- [MDN: Comparison operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators)

## C

- https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/

## Haskell

- https://github.com/i-tu/Hasklig
- https://wiki.haskell.org/Arrow_tutorial
- https://en.wikibooks.org/wiki/Haskell/Understanding_arrows
