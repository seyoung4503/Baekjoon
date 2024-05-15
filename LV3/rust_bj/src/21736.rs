use std::io::{stdin, Read};
use std::any::type_name_of_val;





fn bfs() {

}


fn main() {
    let mut buffer = String::new();
    stdin().read_to_string(&mut buffer).unwrap();
    let mut buffer = buffer.split_ascii_whitespace();

    let n = buffer.next().unwrap().parse::<usize>().unwrap();
    let m = buffer.next().unwrap().parse::<usize>().unwrap();

    let mut matrix: Vec<Vec<char>> = Vec::new();
    let mut matrix: Vec<Vec<usize>> = vec![vec![0; n]; m];
    let start = [0, 0];
    let find_start = false;

    for i in 0..n {
        let line = buffer.next().unwrap();
        let v : Vec<char> = line.chars().collect();
        if find_start == false {
            if let Some(position) = v.iter().position(|&x| x == 'I') {
                find_start = true;
            }
        }
        
        


        matrix.push(v);
        
    }

    println!("{:?}", matrix);


    
    
}