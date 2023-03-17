import pydoodle
c = pydoodle.Compiler(clientId="d8b8e60770492a2a9324ba34e615b720", clientSecret="98069ff551002310a960986d01c1dec7b2606a4d90bb18444967e456c371f05b")
str1=r"""
    #include <stdio.h>
        void main(){
            int a=110;
            printf("hello world\n");
            printf("%d",a);
        }"""
result = c.execute(script=str1, language="c")
usage = c.usage()
print( result.output[0], sep='\n')