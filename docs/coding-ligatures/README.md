# coding-ligatures-README

Special ligatures dedicated for coders. The ligatures are based on the most common character combinations used in languages like Python or JavaScript.

in folder resources you will find resources, that I'm using for this project

## Glyph naming standard

Naming glyphs follows simple formula:

The main part of ligature's name is build with source glyphs' names separated by `_`. Every coding ligature has suffix `.code`.

- `sourceGlyphNameA_sourceGlyphNameB_sourceGLyphNameC.code`

- *example:*
glyph constructed out of `slash` and `asterix` will be named `slash_asterix.code`

#`maybe this should be truth only for the operators? in other situations we would't use underscores?`

## Planning work

Work was divided into 3 stages that corresponds to different priority levels

- *priority 1*

    ### logic operators
    |ligature|name                    |
    |--------|------------------------|
    |==      |equal_equal.code        |
    |!=      |exclam_equal.code       |
    |===     |equal_equal_equal.code  |
    |!==     |exclam_equal_equal.code |
    |=/=     |equal_slash_equal.code  |
    |!!      |exclam_exclam.code      |
    |??      |question_question.code  |
    |%%      |procent_procent.code    |
    |&&      |ampersand_ampersand.code|
    |&#124;&#124;      |bar_bar.code            |
    |?.      |question_period.code    |
    |?:      |question_colon.code     |

    ### math operators
    |ligature|name                    |
    |--------|------------------------|
    |+       |plus.code               |
    |++      |plus_plus.code          |
    |+++     |plus_plus_plus.code     |
    |-       |hyphen.code             |
    |—       |hyphen_hyphen.code      |
    |—-      |hyphen_hyphen_hyphen.code|
    |*       |asterix.code            |
    |**      |asterix_asterix.code    |
    |***     |asterix_asterix_asterix.code|
    |+=      |                        |
    |-=      |                        |
    |*=      |                        |
    |/=      |                        |

    ### comments and others
    |ligature|name                    |
    |--------|------------------------|
    |__      |underscore_underscore.code|
    |/*      |slash_asterix.code      |
    |*/      |asterix_slash.code      |
    |//      |slash_slash.code        |
    |///     |slash_slash_slash.code  |
    |'''     |quotesinge_quotesinge_quotesinge.code|
    |#       |numbersign.code         |
    |##      |numbersign_numbersign.code|
    |###     |numbersign_numbersign_numbersign.code|


- *prority 2*

    `# I'm still not sure about making special brackets`

    ### keywords
    |ligature|name                    |
    |--------|------------------------|
    |var     |                        |
    |const   |                        |
    |let     |                        |
    |if      |                        |
    |else    |                        |
    |elif    |                        |
    |switch  |                        |
    |case    |                        |
    |for     |                        |
    |while   |                        |
    |in      |                        |
    |not     |                        |
    |try     |                        |
    |except  |                        |
    |catch   |                        |
    |assert  |                        |
    |def     |                        |
    |function|                        |
    |class   |                        |
    |self    |                        |
    |print   |                        |
    |and     |                        |
    |or      |                        |
    |return  |                        |
    |true    |                        |
    |True    |                        |
    |false   |                        |
    |False   |                        |
    |do      |                        |

    ### string formatting operators and escape characters
    |ligature|name                    |
    |--------|------------------------|
    |%c      |                        |
    |%d      |                        |
    |%s      |                        |
    |%g      |                        |
    |%r      |                        |
    |\n      |                        |
    |\b      |                        |
    |\r      |                        |
    |\t      |                        |
    |\v      |                        |
    |\'      |                        |
    |\"      |                        |
    |\\      |                        |
    |%%      |                        |

    ### bracket combinations
    |ligature|name                    |
    |--------|------------------------|
    |{[      |braceleft_bracketleft.code|
    |]}      |bracketright_braceright.code|
    |[[      |bracketleft_bracketleft.code|
    |]]      |bracketright_bracketright.code|
    |[(      |bracketleft_parenleft.code|
    |)]      |parenright_bracketright.code|
    |{(      |braceleft_parenleft.code|
    |)}      |parenright_braceright.code|
    |((      |parenleft_parenleft.code|
    |))      |parenright_parenright.code|

- *priority 3*

    ### (more) language specific keywords
    |ligature|name                    |
    |--------|------------------------|
    |import  |                        |
    |#include|                        |
    |void    |                        |
    |int     |                        |
    |str     |                        |
    |char    |                        |
    |float   |                        |
    |double  |                        |
    |long    |                        |
    |alloc   |                        |
    |dealloc |                        |
    |printf  |                        |
    |func    |                        |
    |*argv   |                        |
    |*args   |                        |
    |**kwargs|                        |
    |def     |                        |
    |class   |                        |
    |self    |                        |
    |print   |                        |
    |and     |                        |
    |or      |                        |
    |return  |                        |
    |__init__|                        |
    |__del__ |                        |
    |__iter__|                        |
    |__repr__|                        |


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
# Additional idea:

We could create the stylistic set that "emulates" mark down behaviour. With ligatures for `[]` , `[x]` etc
