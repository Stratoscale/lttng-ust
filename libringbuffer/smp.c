/*
 * libringbuffer/smp.c
 *
 * Copyright (C) 2011-2012 Mathieu Desnoyers <mathieu.desnoyers@efficios.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; only
 * version 2.1 of the License.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

#define _GNU_SOURCE
#define _LGPL_SOURCE
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>
#include "smp.h"

int __num_possible_cpus;


/*
 * parse the /sys/devices/system/cpu/possible file to get the id of maximum cpu
 * the file of the format "number[,-number]*"
 * we are reading the line till we reach the last number
 */
static int _get_max_possible_cpu_id(void)
{
	FILE *file;
	int max_cpu = -1;

	file = fopen("/sys/devices/system/cpu/possible", "r");
	if (!file)
	{
		return -1;
	}

	for (;;) 
	{
		char sep;
		int cpu;
		int n = fscanf(file, "%u%c", &cpu, &sep);
		if (n <= 0)
		{
			break;
		}

		/* condition for one last number left in line, we assume that there is no "\n" at the end of line for this file */
		if (n == 1)
		{
			max_cpu = cpu;
			break;
		}
	}

	fclose(file);
	return max_cpu;
}

void _get_num_possible_cpus(void)
{
	int result;

	/* On Linux , when some processor is missing from configuration ( due to some error during boot )
 	 * _SC_NPROCESSORS_CONF returns the total number of configured processors, and as a result
 	 * getcpu() could return a value greater than sysconf(_SC_NPROCESSORS_CONF). This happends in case the missing processor is not the last one.
 	 * therefore , we need to find the maximum defined processor, and not the number of processors defined.
 	 */
	
	result = _get_max_possible_cpu_id();
	if (result == -1)
		return;
	__num_possible_cpus = result;
}
