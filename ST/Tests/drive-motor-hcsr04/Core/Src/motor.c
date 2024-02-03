#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include "main.h"
#include "stm32f4xx_hal.h"
#include "motor.h"

extern TIM_HandleTypeDef htim2;
extern TIM_HandleTypeDef htim5;

#define MOTOR_EN_B_LEFT htim2
#define MOTOR_EN_A_RIGHT htim5

#define IN1 GPIO_PIN_6
#define IN2 GPIO_PIN_7
#define IN3 GPIO_PIN_0
#define IN4 GPIO_PIN_1

#define  CH_MOTOR_EN_B TIM_CHANNEL_2
#define  CH_MOTOR_EN_A TIM_CHANNEL_1

#define kpx 0.5
#define kix 0.6
#define kdx 0.7
#define delta_time 0.1 // 0.1 segundos que é 100ms

double offset;
double sum_offsets = 0.0;
double P, I, D;
double pre_offset=0;
double PID;

//int status=0;

double pid_control (int x, int y){
	offset = x - 44;
	sum_offsets += offset;
	P = kpx*offset;
	I = kix*sum_offsets;
	D = kdx*((offset - pre_offset)/delta_time);
	pre_offset = offset;
	PID = P + I + D;
	return PID;
}


void motor_backwards(void){
	HAL_GPIO_WritePin(GPIOA, IN1, 0);
	HAL_GPIO_WritePin(GPIOA, IN2, 1);
	HAL_GPIO_WritePin(GPIOB, IN3, 1);
	HAL_GPIO_WritePin(GPIOB, IN4, 0);

	__HAL_TIM_SET_COMPARE(&MOTOR_EN_A_RIGHT,CH_MOTOR_EN_A,42);
	__HAL_TIM_SET_COMPARE(&MOTOR_EN_B_LEFT,CH_MOTOR_EN_B,45);
}

void motor_right(void){
	HAL_GPIO_WritePin(GPIOA, IN1, 1);
	HAL_GPIO_WritePin(GPIOA, IN2, 0);
	HAL_GPIO_WritePin(GPIOB, IN3, 0);
	HAL_GPIO_WritePin(GPIOB, IN4, 1);

	__HAL_TIM_SET_COMPARE(&MOTOR_EN_A_RIGHT,CH_MOTOR_EN_A,30);
	__HAL_TIM_SET_COMPARE(&MOTOR_EN_B_LEFT,CH_MOTOR_EN_B,42);
}

void motor_left(void){
	HAL_GPIO_WritePin(GPIOA, IN1, 1);
	HAL_GPIO_WritePin(GPIOA, IN2, 0);
	HAL_GPIO_WritePin(GPIOB, IN3, 0);
	HAL_GPIO_WritePin(GPIOB, IN4, 1);

	__HAL_TIM_SET_COMPARE(&MOTOR_EN_A_RIGHT,CH_MOTOR_EN_A,42);
	__HAL_TIM_SET_COMPARE(&MOTOR_EN_B_LEFT,CH_MOTOR_EN_B,30);
}

void motor_stright(void){
	HAL_GPIO_WritePin(GPIOA, IN1, 1);
	HAL_GPIO_WritePin(GPIOA, IN2, 0);
	HAL_GPIO_WritePin(GPIOB, IN3, 0);
	HAL_GPIO_WritePin(GPIOB, IN4, 1);

	__HAL_TIM_SET_COMPARE(&MOTOR_EN_A_RIGHT,CH_MOTOR_EN_A,42);
	__HAL_TIM_SET_COMPARE(&MOTOR_EN_B_LEFT,CH_MOTOR_EN_B,45);

}

void motor_stop(void){
	  HAL_GPIO_WritePin(GPIOA, IN1, 0);
	  HAL_GPIO_WritePin(GPIOA, IN2, 0);
	  HAL_GPIO_WritePin(GPIOB, IN3, 0);
	  HAL_GPIO_WritePin(GPIOB, IN4, 0);

	__HAL_TIM_SET_COMPARE(&MOTOR_EN_A_RIGHT,CH_MOTOR_EN_A,0);
	__HAL_TIM_SET_COMPARE(&MOTOR_EN_B_LEFT,CH_MOTOR_EN_B,0);
}

void motor_desvia(uint16_t distancia){
  	while(distancia < 15){
  		motor_backwards();
  		HAL_Delay(750);
  		motor_left();
  		HAL_Delay(1001);
  		break;
  	}
}
