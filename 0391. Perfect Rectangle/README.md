<div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0391. Perfect Rectangle</u></h1></div>
      <img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard">
      <div><table type="1"><th>Array</th><th>Line-Sweep</th></table></div><br>
		<div style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif"><p>
      Given an array rectangles where rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (x<sub>i</sub>, y<sub>i</sub>) and the top-right point of it is (a<sub>i</sub>, b<sub>i</sub>).<br><br>
      Return true if all the rectangles together form an exact cover of a rectangular region. <br>
    </div>
    <br><br>
    <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
      <div><p>
      <strong><u>Example 1:</u></strong><br>
      <strong>Input:</strong> rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]] <br>
      <strong>Output:</strong> true <br>
      <strong>Explanation:</strong><br> 
      <img src="https://github.com/Suresh-J15/LeetCode-Solutions/blob/main/0391.%20Perfect%20Rectangle/Example%201.png" alt="Example 1"  style="width: 40%;"><br>
      All 5 rectangles together form an exact cover of a rectangular region. <br>
    </p></div>
    <div><p>
      <strong><u>Example 2:</u></strong><br>
      <strong>Input:</strong> rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]] <br>
      <strong>Output:</strong> false <br>
      <strong>Explanation:</strong><br>
      <img src="https://github.com/Suresh-J15/LeetCode-Solutions/blob/main/0391.%20Perfect%20Rectangle/Example%202.png" alt="Example 2" style="width: 40%;"><br>
      Because there is a gap between the two rectangular regions. <br>
    </p></div>
  <div><p>
    <strong><u>Example 3:</u></strong><br>
    <strong>Input:</strong> rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]] <br>
    <strong>Output:</strong> false <br>
    <strong>Explanation:</strong><br>
    <img src="https://github.com/Suresh-J15/LeetCode-Solutions/blob/main/0391.%20Perfect%20Rectangle/Example%203.png" alt="Example 2" style="width: 40%;"><br>
    Because two of the rectangles overlap with each other. <br>
  </p></div>
</div>
<br><br>
<div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
  <strong><u>Constraints:</u></strong><br><br>
    <ul>
      <li style="margin-bottom: 13px;">1 <= rectangles.length <= 2 * 10<sup>4</sup> </li>
      <li style="margin-bottom: 13px;">rectangles[i].length == 4</li>
      <li style="margin-bottom: 8px;">-10<sup>5</sup> <= x<sub>i</sub> < a<sub>i</sub> <= 10<sup>5</sup></li>
      <li style="margin-bottom: 8px;">-10<sup>5</sup> <= y<sub>i</sub> < b<sub>i</sub> <= 10<sup>5</sup></li>
    </ul>
</div>
