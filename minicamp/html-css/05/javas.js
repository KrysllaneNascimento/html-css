function calculateIMC(weight, height){
    return weight / (height * height);
}

function start(){
    var buttonCalculateImc = document.querySelector('#button-calculate-imc')
    buttonCalculateImc.addEventListener('click', handleButtonClick)
    handleButtonClick();

    var inputWeight = document.querySelector('#input-weight')
    var inputHeight = document.querySelector('#input-height')

    inputWeight.addEventListener('input', handleButtonClick)
    inputHeight.addEventListener('input', handleButtonClick)
}

function handleButtonClick(){
    var inputWeight = document.querySelector('#input-weight')
    var inputHeight = document.querySelector('#input-height')
    imcResult = document.querySelector("#imc-result")

    var weight = Number(inputWeight.value)
    var height = Number(inputHeight.value)

    var imc = calculateIMC(weight, height)
    //tofixed- pega um valor numerico e converte para (n) casas decimais
    var formatedImc = imc.toFixed(2).replace('.',',')

    imcResult.textContent = formatedImc

}

start();
