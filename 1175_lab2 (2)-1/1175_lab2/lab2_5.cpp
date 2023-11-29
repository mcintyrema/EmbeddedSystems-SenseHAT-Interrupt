#include <sys/time.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void timer_handler(int num){
	static int count = 0;
	struct timeval ts;
	count += 1;
	gettimeofday(&ts, NULL);
	printf("Interrupt occured! Timer has expired\n");
}

int main(){

	struct sigaction sa;
	struct itimerval timer;
	memset(&sa, 0, sizeof(sa));
	sa.sa_handler = &timer_handler;
	sigaction(SIGVTALRM, &sa, NULL);
	timer.it_value.tv_sec = 0;
	timer.it_value.tv_usec = 400000;
	timer.it_interval.tv_sec = 0;
	timer.it_interval.tv_usec = 400000;
	setitimer(ITIMER_VIRTUAL, &timer, NULL);
	while(1);


}
