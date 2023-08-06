
# UIE
Universal Integer Encrypting algorithm.

## USAGE

#### UIE.UIECoder(key, key_mode, result_mode, splitter, dict_)

- key : str - A key for encryption\decryption.
- key_mode : UIEKeyMode - A formatter for key.
- result_mode : UIEResultMode - A result formatter.

##### Encryption:

    UIECoder.encrypt(text)
      This method is returing encrypted data.

      text : str - Data for encrypt.

##### Decryption:

    UIECoder.decrypt(encrypted)
      This method is returning decrypted data.

      encrypted - Encrypted data. (Type from result formatter)

#### UIE.modes

##### UIE.modes.UIEKeyMode

      Key modes:
        UIEKeyMode.uD - Default.
        UIEKeyMode.u1 - sha1 hash.
        UIEKeyMode.u256 - sha256 hash.
        UIEKeyMode.uM5 - md5 hash.

##### UIE.modes.UIEResultMode

      Result modes:
        UIEResultMode.uR - Raw.
        UIEResultMode.uB64 - Base64 encoding.