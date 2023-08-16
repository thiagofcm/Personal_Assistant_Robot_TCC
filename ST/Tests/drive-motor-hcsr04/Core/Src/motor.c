#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include "main.h"
#include "stm32f4xx_hal.h"
#include "motor.h"

extern TIM_HandleTypeDef htim2;

void motor_frente(void){
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, 0);
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_7, 1);

	__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,45);
	TIM5->CCR1=45;
}

void motor_right(void){
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, 0);
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_7, 1);

	__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,45);
	TIM5->CCR1=10;
}

void motor_left(void){
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, 0);
	  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_7, 1);

	__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,10);
	TIM5->CCR1=45;
}

void motor_re(void){
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, 1);
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_7, 0);
	__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,45);
	TIM5->CCR1=45;
}

void motor_parado(void){
	__HAL_TIM_SET_COMPARE(&htim2,TIM_CHANNEL_2,0);
	TIM5->CCR1=0;
}

void motor_desvia(uint16_t distancia){
  	while(distancia < 15){
  		motor_re();
  		HAL_Delay(750);
  		motor_left();
  		HAL_Delay(1001);
  		break;
  	}
}
