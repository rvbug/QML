
<p align="center"> <img height=200 align=center src="https://scitechdaily.com/images/Black-Hole-Accetion-Disc-Art-Illustration-1536x864.jpg"> </p>


---
<p align="center"> <img src="https://img.shields.io/badge/License-GPLv3-blue.svg"> <img height=21  src="https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white"> 
<img height=21  src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</p>



<br>
<br>

---
# Inspiration

My inspiration to work on Quantum Gravity is drawn from [Interstellar](https://en.wikipedia.org/wiki/Interstellar_(film)) by [Nolan](https://en.wikipedia.org/wiki/Christopher_Nolan). 
The black hole shown in the movie uses actual calculations which took more than 100+ hours to render.

Noble Price winer and theoretical physicist [Kip Thorne](https://en.wikipedia.org/wiki/Kip_Thorne), was the scientific consultant for this movie. He is a long time friend and colleague Stephen Hawking and Carl Sagan. 


This [Book](https://en.wikipedia.org/wiki/The_Science_of_Interstellar) explains movie's technical details.


# Basics

<img width="666" alt="image" src="https://github.com/rvbug/q-gravity/assets/10928536/777d6cca-3701-4bd8-8a5d-b0b67b733a65">



<br>

# Quantum Gravity (QG)

Quantum Gravity (QG) helps describe gravity according to the principles of quantum mechanics and will help us to understand what happens near black hole and at the moment of singularity.
<br>

# Rust Topics
<details>
  <summary> Intro to Rust </summary>

  ## Basics

> ## Essentials
rustup - Manages rust installation   
cargo new - create a new binary or library  
  
> ## Print & Format Macros
  Printing is handled by a series of macros defined in std::fmt some of which include. `format!` - writes formatted text to String.   
  Macros expand the coee further and it generates additional code.  
  
  ```rust
  // {:?} - Is the debug print 
  let l = 42;
  println!("The debug version : {life:?}")
  println!("The print version : {life}")

```

> ## Control flow & Loop

`if .. else`  
`if .. else if .. else`  
`loop { ... }`  
`while condition { ... } `  

> ## Size in memory
```rust
let x = 5;
println!("int is {} bytes", std::mem::size_of_val(&x));
```

> ## Crates vs Modules vs Packages
Crates - Either a library or an executable  
Modules - Helps maintain privacy  
Packages - Build test and share crates  
Paths - A way to name structs, functions etc   


> ### Modules
```rust

//utils.rs
pub fn greet() {
    println!("calling from example_use");
}

// main.rs 
pub mod utils;
use utils::greet;

fn main() {
    println!("Hello, world!");

   greet(); 
}
```



> ## Ownership & Borrowing rules
- Every data will have only one onwer
- Two variables cannot point to same memory location
- You can transfer the ownership by assignment, passing value to a func or returning a value from a func

> ## Comments
running `cargo doc` will create a document under taget > doc > all HTML created. run `cargo doc --open` 
```rust
/// Generate library docs for the following item.
//! Generate library docs for the enclosing item.
```



> ## use
```rust
// self - is used to import all public items from a module
//e.g
// event is a submodule from the crate crossterm
event::{self, KeyCode, KeyEventKind},

```
> ## Constants
Always upper case and the value can never change
```
const PI = 3.14
```

> ## Shadowing

```rust
 let mut x = 10;
  {
      x = 20;
  }
  // this prints 20
  println!("{}", x);

let x = "it is now a string
println!("{}, x);

let x = true
println!("{}, x);

```
</details>

<details>
  <summary> Strings, Vectors & Hashmaps </summary>

> ## Strings
```rust
  // String Literal = &str is stored on stack and used when the size is known as compiled time.
  // String Object = String::new() and String::from()
  let stack_name: &str = "hello from stack";
  let heap_name_from = String::from("hello from heap");
  let mut heap_name_new = String::new();
  heap_name_new.push_str("hello from heap new");

  let name = &"rvbug".to_string()[0..4];
  // let show = &name[0..4];
  println!("{}", &name);
```

> ## Vectors
```rust
  let mut vec: Vec<i64> = vec![1,2,3];
  println!("{:?}", &vec);
  vec.push(4);
  println!("{:?}", vec);
```

> ## HashMap

- HashMap - Arrays, Vectors and Tuples -> Ordered data structures which uses index numbers to access the value. HashMap Performance is much better than index based as it uses keys and value to access regardless of the size of the data. It uses Hash tables and in rust it is called as hashmap   

```rust
use std::collections::HashMap;

fn main() {

    let mut maps = HashMap::new();
    maps.insert(1,2);
    maps.insert(3,4);
    maps.insert(5,6);

println!("{:#?} - {:#?}", maps.keys(), maps.values());
println!("{:#?}", maps);

// to remove use
//maps.remove(key)

use std::collections::HashMap;


    let mut map: HashMap<u8, &str> = HashMap::new();
    map.insert(1, "Hello");
    println!("{:?}", map);

    match map.get(&1) {
        Some(&v) => println!("{}", v),
        None => println!("None"),
    }


// using struct
#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

let mut hmap: HashMap<u8, Person> = HashMap::new();
hmap.insert(1, Person { name: "John".to_string(), age: 30 });
println!("{:?}", hmap);



}
```

</details>

<details>
  <summary>Traits & Advanced Traits</summary>

  > ## Traits & Impl
In OOPs, we have data and methods as 1 unit. In rust, data is in Struct/Enum and traits which define the behaviour is kept separately.  
**`Traits allows different type to share the same behaviour`**

```rust

struct Person {
    name: String,
}

struct Animal {
    breed: String,
}

// ideally definition only
trait Eat{
    //default method
    fn eat(&self) {
    println!("Hello please eat default");
  }
}

//implementation details
impl Eat for Person {
  fn eat(&self) {
    println!("
  }
}

//triggers default implementation 
impl Eat for Animal{}

```
  
> ### Advanced Traits
The item is an associate type - A placeholder to add to traits and methods can use this placeholder.This type is unknown till we implement the trait.
If this trait is implement on vector of int then this item will be an int. 


```rust
trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}


```
</details>

<details>
  <summary> Box </summary>

> ## Box
Helps stores dynamically sized data especially during the compile time, e.g. user input and it ca also grow and shrink dynamically. Especially when you want to transfer large amount of data without expensive copy/clone.
Or Want to own a value by it's particular trait and not by specific type.

All three (Box<T>, Vec<T>, HashMap<K, V>) manage ownership of their data. When they go out of scope, the memory is automatically deallocated.  
Box<T> is ideal for storing a single dynamically sized value.  
Vec<T> is better for storing collections of the same type, where the size can change.  
HashMap<K, V> is efficient for storing key-value pairs, allowing fast lookups based on keys.  

```rust


```
</details>


<details>
  <summary> Results </summary>

> ## Result
```rust
fn divide(a:i32, b:i32) -> Result<i32, String> {
    if b == 0 {
        Err("Error divide by zero".to_string())
    } else {
        Ok(a/b)
    }
}

fn main() {
    let result = divide(10, 0);
    match result {
        Ok(x) => println!("Result = {}", x),
        Err(e) => println!("Error = {}", e)
    }
}
```

</details>


<details>
  <summary>Structs & Enums </summary>

> ## Structure
Creating related data together

```rust
struct Point (u8, u8, u8);

impl Point {
    fn display_point(& self) {
        println!("Point is {} {} {} ", self.0, self.1, self.2);
    }

    fn twice(&self) -> Self {
        Point(self.0 * 2, self.1 * 2, self.2 * 2)
    }

    fn mut_twice(&mut self) -> Self {
        self.0 *= 2;
        self.1 *= 2;
        self.2 *= 2;
        Point(self.0, self.1, self.2)
    }
}

// to call you can use this in main function
let p = Point(1, 2, 3);
// this will not change the point 
p.twice().display_point();
// if I call just the display, it will show the original value
p.display_point();
// another way of calling this is
p = Point::twice(&self)
p.display_point();
// I want to modify the original point itself
let mut p = Point(1,2,3);
p.mut_twice.display_point();
// another way of calling this is
p = Point::mut_twice(&mut self)
p.display_point();

```

> ## Enums 
For grouping related things and use for choice. Associated values are also a feature to store additional data.
``` rust

// simple enums
enum Animal {
cat,
dog,
}

// associate values

enum Shapes {
  Square {length : f64}
  Circle { radius : f64 }
}

// we can also use if let
if let Shapes:: Square {length} == Square {
  ....
}


```

</details>

<details>
  <summary> Iterators </summary>
 > ## Iterators
 If you use iter_into() then it will own the data instead of slices

```rust
# references
let values = vec![1,2,3,4,5];
let mul_by_2 = |x| x * 2;
let new_values = values.iter().map(mul_by_2).collect::<Vec<i32>>();
println!("{:?}", new_values);

```
</details>

<details>
  <summary> Options </summary>
  
> ## Options
will either have a value or none
```rust

 let name: Option<String> = Some("John".to_string());

  //safe unwrap the values
  match name {
    Some(name) => println!("Hello, {}!", name),
    None => println!("Hello, world!"),

  } 

// unsafe unwrap the values
 name.expect()

//forced unwrap
name.unwrap()

// if variable is mut then
let mut age: Option<&u8> = Some(20)
match age.mut()
// ... 

let unwrapped = name.unwrap_or_else( || {
// ...
}

// check if there is a value
// use is_some or is_null
if name.is_some() {
//  ...
} else { ...}

```
</details>

<details>
  <summary> Closures </summary>

> ## Closures
Closures are functions with no name. Closures can access variables outside it's body and also can be passed to a function.  

> ### Simple Closures
```rust

// basic
// let variable_name = | paramerters | -> Return type {
//    BODY
//  }

let sum = |a : i32, b : i32|  a + b;
let prd = |a:  i32, b: i32 | a * b; 
println("Sum is {}", sum(10, 20));
println!(Product is {}", prd(10,20));

```
> ### Closures in function
```rust
    fn use_closures<T>(a:i32, b:i32, func:T) -> i32 
        where T: Fn(i32, i32) -> i32 { 
        func(a, b)
    }
    
    use_closures(10, 20, |a, b| a + b);
    use_closures(10, 20, |a, b| a * b);

    let sum = |a : i32, b : i32|  a + b;
    let prd = |a:  i32, b: i32 | a * b; 

    println!("Sum is {}", use_closures(10, 20, sum));
    println!("product is {}", use_closures(10,20, prd));


```
</details>

<details>
  <summary> Smart Pointers </summary>
  When you know the size of the memory during compile time then it is static memory allcoation (on stack) otherwise it is called dynamic memory allocation (on heap).
  e.g. `let x: 132 = 5` allocates 4 bytes at compile time. 
  
> ## Box
Box is used when you have large amount of data stored on the heap and pointers are stored on the stack.
```rust



```
</details>

<details>
  <summary> Other Topics </summary>

- Error Handling
- Generics
- Lifetimes
- Automated Test
- I/O project
- Iterators 
- Cargo 
- Crates
- Concurrency
- OOPs
- Patterns and Matching

Advanced
- Unsafe Rust
- Advanced Traits & Traits objects
- Advanced types
- Advanced func and closures
- Macros
- &str & String
- Stack vs Heap
- #[derive(Debug)]
- Associated types 
- Processes
- Threads (how to view processes and their associated threads - project)
- Blog to write on how the threads, processes work in Rust - Detailed one
- Async Await

</details>


<br>

---
# References

* [arXiv](https://arxiv.org/)
* [Interstellar](https://en.wikipedia.org/wiki/Interstellar_(film))
* [Thought Experiment](https://en.wikipedia.org/wiki/Einstein%27s_thought_experiments)
* [Interstellar Visualization](https://www.space.com/27692-science-of-interstellar-infographic.html)
* [Quil](https://github.com/quil-lang/quil)
* [quil-rs](https://docs.rs/quil-rs/latest/quil_rs/)
* [qcs](https://docs.rs/qcs/latest/qcs/)
* [Autograd](https://docs.rs/autograd/latest/autograd/)
* [NDArray](https://docs.rs/ndarray/0.15.6/ndarray/)
* [NLOpt](https://docs.rs/nlopt/latest/nlopt/)  
* [roqoqo](https://hqsquantumsimulations.github.io/qoqo_examples/)  
* [Plotter](https://plotters-rs.github.io/book/basic/overview.html)   
* [Relativity](https://geometry-of-relativity.net/rotations-in-spacetime/)    
* [rustworkx](https://github.com/Qiskit/rustworkx/tree/main)    
* [Petgraph](https://docs.rs/petgraph/0.6.4/petgraph/index.html)    
* [MdBook](https://rust-lang.github.io/mdBook/guide/creating.html)      
* [Rust Book](https://doc.rust-lang.org/book/)  
* [Rust by examples](https://doc.rust-lang.org/rust-by-example/hello/print/print_debug.html)    
* [System Design](https://github.com/systemdesign42/system-design)    
* [Cargo Build](https://doc.rust-lang.org/cargo/commands/build-commands.html)   
* [Rust Practice](https://doc.rust-lang.org/)  
* [Rust for Rustaceans](https://rust-for-rustaceans.com/)


