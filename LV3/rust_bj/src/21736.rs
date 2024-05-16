use std::io::{stdin, Read};
use std::any::type_name_of_val;





fn bfs(let start_position) {
    let mut mat: Vec<Vec<usize>> = Vec::new();

    mat.push(start_position);
    
    for i in 0..4 {

    }
}


fn main() {
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();
    let mut buffer = buffer.split_ascii_whitespace();

    let n = buffer.next().unwrap().parse::<usize>().unwrap();
    let m = buffer.next().unwrap().parse::<usize>().unwrap();

    let mut matrix: Vec<Vec<char>> = Vec::new();
    let mut matrix2: Vec<Vec<usize>> = vec![vec![0; n]; m];
    let mut start = [0, 0];
    let mut find_start = false;

    for i in 0..n {
        let mut line = String::new();
        stdin().read_line(&mut line).unwrap();

        let mut v : Vec<char> = line.chars().collect();
        v.pop();

        if find_start == false {
            if let Some(position) = v.iter().position(|&x| x == 'I') {
                find_start = true;
                start[0] = i;
                start[1] = position;
            }
        }

        matrix.push(v);

        

    }
    // let start = [0, 0];
    // let mut find_start = false;

    // for i in 0..n {
    //     let line = buffer.next().unwrap();
    //     // let v : Vec<char> = line.chars().collect();
    //     // if find_start == false {
    //     //     if let Some(position) = v.iter().position(|&x| x == 'I') {
    //     //         find_start = true;
    //     //     }
    //     // }
    //     println!("{:?}", line);
    //     // matrix.push(v);
        
    // }

    println!("{:?}", matrix);
    println!("{:?}", start);


    
    
}