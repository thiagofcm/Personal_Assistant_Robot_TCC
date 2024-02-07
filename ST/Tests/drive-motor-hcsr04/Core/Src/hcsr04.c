#include "main.h"
#include "stdio.h"
#include "stm32f4xx_it.h"
#include "stm32f4xx_hal_tim.h"
#include "hcsr04.h"
extern TIM_HandleTypeDef htim1;

void Delay_us (uint16_t time){
  	__HAL_TIM_SET_COUNTER(&htim1,0);
  	while (__HAL_TIM_GET_COUNTER(&htim1) < time);
}

//uint16_t getDistance(){
//	return distance;
//}

void Read_HCSR04(void){
  	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_9, 1);
  	Delay_us(10);
  	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_9, 0);
  	__HAL_TIM_ENABLE_IT(&htim1, TIM_IT_CC1);
}
