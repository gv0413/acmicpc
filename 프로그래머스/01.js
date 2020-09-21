function solution(progresses, speeds) {
  var answer = [];
  var progressDate = [];
  for(let i=0; i<=progresses.length-1; i++){
      progressDate[i] = Math.ceil((100-progresses[i])/speeds[i]);
  }
  console.log(progressDate);
  // for(let i=0; i<progressDate.length-1; i++){
  //     if(progressDate[i] > progressDate[i+1]){
  //         answer.unshift([progressDate...i+1].length);
  //     }
  // }
  for(let i=0; i<progressDate.length-1; i++){
      for(let j=i+1; j<progressDate.length; j++){
          if(progressDate[i] > progressDate[j]){
              answer.unshift(progressDate[...j].length);
          }   
      }
  }
  console.log(answer);
  return answer;
}