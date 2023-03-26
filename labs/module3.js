// Module 3 PreLab (optional)

// In this PreLab you will write the code to control player movement through a 2d grid of a simple puzzle game inspired by the 1991 hit game Chip's Challenge. This is a 2d grid-based puzzle game where the player collects chips to unlock the exit while avoiding hazards and using keys to unlock doors. Save your code from this PreLab as you'll combine it with code you'll write in other parts of the course to develop the game one piece at a time.

// As is common in grid-based games the map for each level will be represented by an array of arrays with integer values where each integer represents a different type of tile. For this game we will have the following tile types with corresponding integers

// Each level is an array of arrays with integer values
// 0	floor	where the player can walk freely
// 1	wall	the player cannot walk through walls
// 2	crystal	increases the player's crystal count by 1 and turns this into a floor tile
// 3	locked door	acts as a wall. If the player walks into this while they have a key the door will change to a floor tile and the player will lose/use one key
// 4	key	increases the player's key count by 1 and turns this tile into a floor
// 5	lava	kills the player unless the player collected the protective boots
// 6	boots	collects the protective boots and turns this tile into a floor tile
// 7	exit	acts as a wall. If the player collected every crystal on the map the player advances to the next level

// The tiles are stored in row major order starting with the upper left corner (Note: This means the y-axis is inverted. Decreasing the y-coordinate move up on the map). For example if the grid is [[1,1,1],[0,2,7],[1,1,1]] then the level will be played on a 3x3 grid where the top and bottom rows of the level are all wall tiles and the center row, from left to right, contains a floor tile, a crystal, and the exit. If the player starts on the left-most tile of the second row they would be able to move to the right twice to complete the level. To access a tile we will use [x, y] coordinates where x is the column number and y is the row number starting from the upper left corner and counting from 0. This allows for the tile points to correspond with the array indices. For example, the exit would be at the point [2, 1] and would be accessed with grid[1][2]

// Finally, a level will be represented as an object with the keys "grid" which stored the 2d array of tiles and "start" which is an array with 2 integers in the format [x, y] which is where the player starts the level

function movePlayer(levelObject, firstMove){
    let level = JSON.parse(levelObject);
    // "w" for up, "a" for left, "s" for down, and "d" for right
    let grid = level["grid"]; // grid[y][x] y is row, x is column
    let initialPos = level["start"]; 
    let currentPos;
    
}