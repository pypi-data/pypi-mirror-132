- Description:
	```
	This module supply two objects - compare_objects, compare_objects_with_info.
	Each one gets two objects from each type, nested by multiple types and compare it -
		compare_objects - 
		    Test if the object are equal.
            -   return True / False 
			
		compare_objects_with_info - 
		    Test if the object are equal.
            -   return (True / False, <info>) 
	```

- Usage:
    - Imports:
        ```
        from compare_objects import compare_objects
        from compare_objects import compare_objects_with_info
        ```
    
	- compare_objects:
		```
		object_a = {<nested_object>}
        object_b = {<nested_object>}
        
        result = compare_objects(object_a, object_b)
		```
		
    - compare_objects_with_info:
		```
		object_a = [<nested_object>]
        object_b = [<nested_object>]
        
        result, info = compare_objects(object_a, object_b)
		```

- Support:
    ````
    Email me for support: elyashiv3839@gmail,co,.local