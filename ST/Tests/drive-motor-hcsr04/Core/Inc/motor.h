#ifndef MOTOR_H_
#define MOTOR_H_

void motor_stright(void);

void motor_right(void);

void motor_left(void);

void motor_backwards(void);

void motor_stop(void);

double pid_control(int x, int y);

//void motor_handle();

void motor_desvia(uint16_t distancia);

#endif /* MOTOR_H_ */
