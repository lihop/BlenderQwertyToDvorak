
if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data

    def remap(keys):
        if isinstance(keys, (list, tuple, dict)):
            for k in keys:
                if isinstance(k, (list, tuple)):
                    remap(k)
                elif isinstance(k, dict):
                    #print(type(k))
                    #print(k)
                    
                    if 'type' in k:
                        dvorakKey = q_to_d.get(k["type"], None)
                        if dvorakKey != None:
                            print(f'Remapping {k["type"]} -> {dvorakKey}')
                            k["type"] = dvorakKey
                    else:
                        for (dicKey, dicValue) in k.items():
                            remap(dicValue)
                        
    remap(keyconfig_data)

    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)
