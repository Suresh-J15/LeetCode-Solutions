<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <div style="font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><h1><u>0145. Binary Tree Postorder Traversal</u></h1></div>
        <img src="https://img.shields.io/badge/Difficulty-Easy-blue" alt="Difficulty: Easy">
        <div><table type="1"><th>Stack</th><th>Binary Tree</th><th>Tree</th><th>Depth-First Search</th></table></div><br>
        <div style="color: black; font-size: 18px; text-align: left; background-color: lightgray; padding: 20px; border: 1px solid #ccc; font-family: Arial, Helvetica, sans-serif">
          <p>Given the <strong>root</strong> of a binary tree, return the postorder traversal of its nodes' values.</p>
        </div>
        <br><br>
        <div style="background-color: floralwhite; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <div><p>
                <strong><u>Example 1:</u></strong><br>
                <strong>Input:</strong> root = [1,null,2,3] <br>
                <strong>Output:</strong> [3,2,1] <br>
            </p></div>
            <div><p>
                <strong><u>Example 2:</u></strong><br>
                <strong>Input:</strong> root = [1,2,3,4,5,null,8,null,null,6,7,9] <br>
                <strong>Output:</strong> [4,6,7,5,2,9,8,3,1] <br>
            </p></div>
            <div><p>
                <strong><u>Example 3:</u></strong><br>
                <strong>Input:</strong> root = [] <br>
                <strong>Output:</strong> [] <br>
            </p></div>
            <div><p>
                <strong><u>Example 4:</u></strong><br>
                <strong>Input:</strong> root = [1] <br>
                <strong>Output:</strong> [1]
            </p></div>
        </div>
        <br><br>
        <div style="background-color:lavender; font-size: 18; font-family: Arial, Helvetica, sans-serif; padding: 20px;">
            <strong><u>Constraints:</u></strong><br><br>
            <ul>
                <li>The number of nodes in the tree is in the range [0, 100].</li>
                <li>-100 <= Node.val <= 100</li>
            </ul>
        </div>
    </body>
</html>
