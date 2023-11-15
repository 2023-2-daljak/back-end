from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, reverse, render
from django.views.generic import View
from users.models import User
from . import models, forms
from django.shortcuts import render, get_object_or_404


def go_conversation(request, a_pk, b_pk):
    a_pk = request.user.pk
    user_one = User.objects.get(pk=a_pk)
    user_two = get_object_or_404(User, pk=b_pk)

    sorted_user_ids = sorted([user_one.pk, user_two.pk])

    # 대화 상대방과의 대화가 이미 존재하는지 확인합니다.
    conversation = models.Conversation.objects.filter(
        participants__id=sorted_user_ids[0]
    ).filter(
        participants__id=sorted_user_ids[1]
    ).first()

    # 이미 존재하는 대화방으로 이동하거나, 없으면 새로운 대화방을 생성합니다.
    if conversation:
        return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))
    else:
        new_conversation = models.Conversation.objects.create()
        new_conversation.participants.add(user_one, user_two)
        return redirect(reverse("conversations:detail", kwargs={"pk": new_conversation.pk}))


class ConversationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get(pk=pk)
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))
