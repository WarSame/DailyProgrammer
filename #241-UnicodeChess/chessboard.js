
function main(){
	var currBoard="rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR".split("/");
	printRows(currBoard);
	
	var moves=["e2-e4","c7-c5","f1-c4","g8-f6","c4-f7",
	           "e8-f7","e4-e5","d7-d5"];
	
	for (var j=0;j<moves.length;j++){
		currBoard=move(currBoard,moves[j]);
		printRows(currBoard);
		alert("next move");
	}
}
function getColumn(charCol){
	return charCol.charCodeAt(0)-97;
}
function move(board,moveString){
	var startCol=getColumn(moveString[0]);
	var startRow=moveString[1]-1;
	var pieceVal = board[startRow][startCol];
	
	var endCol=getColumn(moveString[3]);
	var endRow=moveString[4]-1;
	
	var newBoard = board;
	
	newBoard[startRow]=newBoard[startRow].substring(0,startCol)+"e"+newBoard[startRow].substring(startCol+1,8);
	newBoard[endRow]=newBoard[endRow].substring(0,endCol)+pieceVal+newBoard[endRow].substring(endCol+1,8);
	return newBoard;
}

function printRows(boardRows){
	for (var i=0;i<8;i++){
		var rowString = getRowString(boardRows[i],i);
		setRowElement(i,rowString);
	}
	document.getElementById('chessboardletters').innerHTML="  ABCDEFGH";
}

function getRowString(inRow,rowNum){
	var rowString="";
	for (var i = 0;i<inRow.length;i++){
		var currChar = inRow[i];
		switch (currChar){
		case "k":
			rowString+="\u265A";
			break;
		case "q":
			rowString+="\u265B";
			break;
		case "r":
			rowString+="\u265C";
			break;
		case "s":
			rowString+="\u265C";
			break;
		case "b":
			rowString+="\u265C";
			break;
		case "n":
			rowString+="\u265E";
			break;
		case "p":
			rowString+="\u265F";
			break;
		case "K":
			rowString+="\u2654";
			break;
		case "Q":
			rowString+="\u2655";
			break;
		case "R":
			rowString+="\u2656";
			break;
		case "S":
			rowString+="\u2656";
			break;
		case "B":
			rowString+="\u2657";
			break;
		case "N":
			rowString+="\u2658";
			break;
		case "P":
			rowString+="\u2659";
			break;
		case "e":
			if ((rowNum+i)%2==0){
				rowString+="\u2610";
			}
			else {
				rowString+="\u2612";
			}
			break;
		}
	}
	return rowString;
}
function setRowElement(rowNum,rowString){
	var rowElement = document.getElementById('chessboard'+rowNum);
	var rowString=8-rowNum+rowString;
	rowElement.innerHTML=rowString;
}