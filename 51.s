	.file	"51.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"world"
	.text
	.p2align 4,,15
	.globl	f1
	.type	f1, @function
f1:
.LFB11:
	.cfi_startproc
	movl	$.LC0, %edi
	jmp	puts
	.cfi_endproc
.LFE11:
	.size	f1, .-f1
	.section	.rodata.str1.1
.LC1:
	.string	"hello world"
	.text
	.p2align 4,,15
	.globl	f2
	.type	f2, @function
f2:
.LFB12:
	.cfi_startproc
	movl	$.LC1, %edi
	jmp	puts
	.cfi_endproc
.LFE12:
	.size	f2, .-f2
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB13:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$.LC0, %edi
	call	puts
	movl	$.LC1, %edi
	call	puts
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE13:
	.size	main, .-main
	.ident	"GCC: (GNU) 6.2.1 20160830"
	.section	.note.GNU-stack,"",@progbits
