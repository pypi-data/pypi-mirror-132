## Light ECDSA

Minimalist and lightweight implementation of ecdsa in python

### usage

Basic private and public key generation and sign a message

```python
from ecdsa import sign, verify, PrivateKey

def main ():
    private_key = PrivateKey()
    public_key  = private_key.generate_public_key() 
    message = b"hello world"
    
    signature = sign(private_key, message)
    valid = verify(public_key, signature, message):
    print(valid)
    
if __name__ == "__main__":
    main()
```

```bash
frijolito@notebook12gb:~/projects/light-ecdsa$ python3 test.py
True
```
