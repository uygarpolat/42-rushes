/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush00.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: upolat <upolat@student.hive.fi>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/20 20:08:13 by upolat            #+#    #+#             */
/*   Updated: 2025/01/20 21:40:04 by upolat           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar(char c);

void	rush(int x, int y)
{
	int	i;
	int	j;

	if (x < 1 || y < 1)
		return ;
	i = -1;
	while (++i < y)
	{
		j = 0;
		while (j < x)
		{
			if (i == 0 && j == 0)
				ft_putchar('/');
			else if ((i == 0 && j == x - 1) || (i == y - 1 && j == 0))
				ft_putchar('\\');
			else if (i == y - 1 && j == x - 1)
				ft_putchar('/');
			else if (i == 0 || j == 0 || i == y - 1 || j == x - 1)
				ft_putchar('*');
			else
				ft_putchar(' ');
			j++;
		}
		ft_putchar('\n');
	}
}
