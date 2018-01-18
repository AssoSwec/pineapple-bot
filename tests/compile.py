from hackerrank.HackerRankAPI import HackerRankAPI

key = "hackerrank|1093226-2147|d254e41b7b952d546e145cace83db907693971d3"
compiler = HackerRankAPI(api_key = key)

source = """
for i in range(5):
    print i
"""


sample_msg = """:compile cpp
```
#include <iostream> 
int main() { 
    std::cout << "hello world" << std::endl; 
    return 0;
}
```
"""

# if sample_msg.startswith(":compile"):
#     arr = sample_msg.split('```')

#     lang = arr[0].split(' ')[1]
#     source = arr[1]

#     result = compiler.run({
#         'source': source,
#         'lang':'cpp'
#     })

#     out = result.output
#     if out != None:
#         print(str(out[0]))
#     else:
#         print(result.message)

s = compiler.supportedlanguages()
print(s)
